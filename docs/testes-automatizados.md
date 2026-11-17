# Testes automatizados

## Como executar localmente

Com Python 3.12 instalado, execute na raiz do repositório:

```bash
python -m pip install -r requirements-dev.txt
coverage run -m unittest discover -s tests -v
coverage report -m
coverage xml
```

O comando de testes apresenta cada caso executado e seu resultado (`ok`). O relatório de cobertura informa a porcentagem de linhas executáveis do módulo de persistência de produtos localizado em `docs/docs/docs/app/app/app/models.py`.

## Escopo dos testes

A suíte verifica:
- abertura da conexão SQLite;
- criação e estrutura da tabela de produtos;
- gravação e leitura de um produto;
- execução repetida da criação da tabela;
- restrições de integridade para preço, quantidade, nome e categoria.

Os testes usam um banco SQLite temporário, isolado dos dados do projeto.

## Limite da métrica

A porcentagem gerada nesta etapa corresponde ao módulo Python de persistência testado. Ela não representa cobertura de todo o JavaScript da interface web. Os testes de banco validam a integração entre o código do modelo e o SQLite; não há, nesta versão, uma suíte automatizada de navegador.
