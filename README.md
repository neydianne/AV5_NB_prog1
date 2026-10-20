## Criar o repositório no GitHub
1. No site do GitHub,  em Repositories e clique em New.
2. Coloque nome e descrição, escolha Public e, se quiser, marque Add a README file.
3. Clique em Create repository.

## 2. Entrar na conta do GitHub no VS Code
1. Clique no ícone de conta no canto inferior esquerdo.
2. Escolha a opção Sign in to use GitHub / Sign in with GitHub.
3. O navegador vai abrir pedindo autorização. Clique em Autorizar.
4. Volte para o VS Code, sua conta já estará conectada.

## 3. Clonar o repositório
1. No VS Code, feche qualquer pasta aberta.
2. Na aba Explorer, clique em Clone Repository.
3. Escolha Clone from GitHub, selecione seu perfil e depois o repositório.
4. Escolha a pasta de destino. Pronto, o repositório foi copiado para o seu computador.

## 4. Configurar nome e e-mail
Abra o terminal do VS Code dentro da pasta do repositório e rode:
git config user.name "neydianne"
git config user.email "neydiannecarvalho26@gmail.com"
As aspas são necessárias.

## 5.Enviar suas alterações
1. Puxe as novidades primeiro com git pull. Isso evita conflitos.
2. Alterações no código.
3. Na aba Source Control, faça o stage das alterações (clique no +, é o mesmo que git add).
4. Escreva a mensagem do commit. 
5. Clique em Commit.
6. Clique em Sync Changes (faz o push) e as mudanças vão para o GitHub.
6.Usando o uv
pip install uv
uv init
uv add sqlalchemy pymysql python-dotenv
uv run consulta.py
1. Instala o uv.
2. Inicializa o projeto.
3. Instala as bibliotecas.
4. Roda o código.
