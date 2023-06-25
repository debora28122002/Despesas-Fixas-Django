# Despesas Fixas Django

Bem-vindo ao Despesas Fixas - Django, um aplicativo web para gerenciar suas despesas fixas mensais, onde você pode adicionar/editar/excluir/visualizar a despesa e o valor atribuído a ela.

## Tecnologias Utilizadas

- Python
- Django
- HTML
- CSS

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python (versão 3.6 ou superior)
- Django (versão 3.0 ou superior)

## Como Executar o Projeto

1. Clone o repositório:
   ```
   git clone https://github.com/debora28122002/Despesas-Fixas-Django.git
   ```
2. Acesse o diretório do projeto:
   ```
   cd Despesas-Fixas-Django
   ```
3. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   ```
   - Ativar: no Windows:
   ```
   venv\Scripts\activate
   ```
   - Ativar: no Linux/Mac:
   ```
   source venv/bin/activate
   ```
4. Execute as migrações do banco de dados:
   ```
   python manage.py migrate
   ```
5. Inicie o servidor de desenvolvimento:
   ```
   python manage.py runserver
   ```
6. Acesse o aplicativo no seu navegador web em `http://localhost:8000/`.

## Rotas

Esta aplicação utiliza as seguintes rotas definidas no arquivo `despesas_fixas/urls.py`:

- `/`: Página inicial que exibe a visão geral das despesas fixas.
- `despesas_fixas/despesa/`: Página de criação de uma nova despesa fixa.
- `despesas_fixas/despesa/delete/<int:id_despesa>/`: Página de exclusão de uma despesa fixa existente.
- `/despesas_fixas/despesa/submit`: Página de edição de uma despesa fixa existente.

## Contribuindo

Contribuições são bem-vindas! Se você deseja contribuir com esta aplicação Web e torná-lo ainda melhor, sinta-se à vontade para abrir issues ou enviar pull requests. Certifique-se de que suas contribuições estejam alinhadas com os padrões de código e diretrizes do projeto.

## Contato
Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato comigo pelo e-mail dbrdejesus15@gmail.com.
