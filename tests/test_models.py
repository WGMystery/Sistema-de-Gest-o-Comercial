import os
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch

# The original model is kept in the application's existing directory.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(
    ROOT, "docs", "docs", "docs", "app", "app", "app"
)
sys.path.insert(0, MODEL_DIR)

import models


class ProductModelTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.database_path = os.path.join(self.temp_dir.name, "test_gestao.db")
        self.database_patch = patch.object(models, "DATABASE", self.database_path)
        self.database_patch.start()

    def tearDown(self):
        self.database_patch.stop()
        self.temp_dir.cleanup()

    def test_connect_creates_database_connection(self):
        connection = models.conectar()
        try:
            self.assertIsInstance(connection, sqlite3.Connection)
            self.assertTrue(os.path.exists(self.database_path))
        finally:
            connection.close()

    def test_create_products_table_and_persist_product(self):
        models.criar_tabela_produtos()
        connection = models.conectar()
        try:
            columns = connection.execute("PRAGMA table_info(produtos)").fetchall()
            self.assertEqual(
                [column[1] for column in columns],
                ["id", "nome", "categoria", "preco", "quantidade", "descricao"],
            )

            connection.execute(
                """
                INSERT INTO produtos (nome, categoria, preco, quantidade, descricao)
                VALUES (?, ?, ?, ?, ?)
                """,
                ("Caderno", "Papelaria", 12.50, 8, "Caderno universitário"),
            )
            connection.commit()
            product = connection.execute(
                "SELECT nome, categoria, preco, quantidade, descricao FROM produtos"
            ).fetchone()
            self.assertEqual(
                product,
                ("Caderno", "Papelaria", 12.5, 8, "Caderno universitário"),
            )
        finally:
            connection.close()

    def test_create_table_is_safe_to_run_more_than_once(self):
        models.criar_tabela_produtos()
        models.criar_tabela_produtos()
        connection = models.conectar()
        try:
            count = connection.execute(
                "SELECT COUNT(*) FROM sqlite_master "
                "WHERE type = 'table' AND name = 'produtos'"
            ).fetchone()[0]
            self.assertEqual(count, 1)
        finally:
            connection.close()

    def test_database_rejects_negative_price(self):
        models.criar_tabela_produtos()
        connection = models.conectar()
        try:
            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute(
                    "INSERT INTO produtos (nome, categoria, preco, quantidade) "
                    "VALUES (?, ?, ?, ?)",
                    ("Produto inválido", "Teste", -1, 1),
                )
        finally:
            connection.close()

    def test_database_rejects_negative_quantity(self):
        models.criar_tabela_produtos()
        connection = models.conectar()
        try:
            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute(
                    "INSERT INTO produtos (nome, categoria, preco, quantidade) "
                    "VALUES (?, ?, ?, ?)",
                    ("Produto inválido", "Teste", 10, -1),
                )
        finally:
            connection.close()

    def test_database_requires_product_name_and_category(self):
        models.criar_tabela_produtos()
        connection = models.conectar()
        try:
            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute(
                    "INSERT INTO produtos (categoria, preco, quantidade) "
                    "VALUES (?, ?, ?)",
                    ("Teste", 10, 1),
                )
            with self.assertRaises(sqlite3.IntegrityError):
                connection.execute(
                    "INSERT INTO produtos (nome, preco, quantidade) "
                    "VALUES (?, ?, ?)",
                    ("Produto", 10, 1),
                )
        finally:
            connection.close()


if __name__ == "__main__":
    unittest.main()
