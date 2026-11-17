# Identificação Curricular e Planejamento

## Problema comunitário
Um pequeno empreendimento comercial enfrenta dificuldades para organizar e controlar suas atividades diárias, pois vendas, estoque e pedidos são registrados manualmente. Isso gera perda de tempo, dificuldade para localizar informações e possibilidade de erros.

## Público direto
Proprietário, responsável pela administração e funcionários do pequeno empreendimento, com conhecimentos básicos de tecnologia.

## Público indireto
Clientes, moradores, familiares e demais membros da comunidade.

## Solução proposta
Desenvolvimento de uma aplicação web simples e responsiva para cadastrar, consultar e editar informações essenciais do empreendimento.

## Soluções semelhantes analisadas

### MarketUP
https://marketup.com/versoes/

### Kyte
https://www.kyteapp.com/pt/controle-de-vendas

As soluções oferecem recursos de cadastro de produtos, vendas e controle de estoque. O diferencial do projeto será a simplicidade da interface e sua adaptação às necessidades do pequeno empreendimento.

## Modularização
O sistema será dividido em módulos menores, com responsabilidades específicas, facilitando desenvolvimento, testes e manutenção.

## Usabilidade
A interface será intuitiva, com campos organizados, textos claros e navegação simples.

## Competência profissional
Desenvolver soluções tecnológicas utilizando conhecimentos de análise, projeto, implementação e manutenção de sistemas computacionais.

## Arquitetura
Arquitetura monolítica em camadas utilizando o padrão MVC.

### Model
Responsável pelo gerenciamento dos dados.

### View
Responsável pela interface apresentada ao usuário.

### Controller
Responsável pelo processamento das ações e regras do sistema.

## Tecnologias utilizadas
- Python 3.12: linguagem principal.
- Flask 3.x: framework para aplicação web.
- HTML5: estrutura das páginas.
- CSS3: aparência das interfaces.
- SQLite: armazenamento de dados.

## Entidades principais
- Produto.
- Venda.

## Requisitos funcionais
- Cadastrar produtos.
- Consultar produtos.
- Editar informações.
- Registrar vendas.
- Consultar estoque.
- Exibir alertas de estoque baixo.

## Requisitos de segurança
- Validar campos obrigatórios.
- Impedir preços e quantidades negativos.
- Exibir mensagens de erro claras.
- Evitar coleta desnecessária de dados pessoais.
