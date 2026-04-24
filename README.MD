## Coffee Kitty

Projeto web desenvolvido com Django que simula uma cafeteria temática inspirada na Hello Kitty.  
O sistema permite visualizar categorias, produtos, informações da loja e gerenciar uma lista de desejos.

---

# Funcionalidades

- Autenticação de usuários (login/logout)
- Visualização de categorias
- Visualização de produtos (cardápio)
- Adição e remoção de itens na lista de desejos
- Interface responsiva (mobile + desktop)
- Interface estilizada (tema Coffee Kitty)
- Rotas protegidas com autenticação
- Página 404 personalizada

---

# Tecnologias utilizadas

- Python
- Django
- HTML
- CSS
- SQLite

---

# Estrutura do projeto

```
coffeekitty/
│
├── cafeteria/ # App principal
│ ├── models.py # Modelos (Categoria, Produto, ListaDesejos)
│ ├── views.py # Lógica do sistema
│ ├── urls.py # Rotas do app
│
├── templates/ # Templates HTML
│ ├── base.html
│ ├── home.html
│ ├── cardapio.html
│ ├── lista.html
│ ├── informacoes.html
│ ├── login.html
│ ├── 404.html
│
├── static/ # Arquivos estáticos (CSS, imagens)
│ └── cafeteria/
│
├── media/ # Uploads (imagens de produtos/categorias)
│
├── db.sqlite3 # Banco de dados
├── manage.py
```

---

# COMO RODAR O PROJETO

## 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd CoffeKitty
```

2. Criar ambiente virtual
```bash
python -m venv venv
```

3. Ativar ambiente virtual
Windows:
```bash
venv\Scripts\activate
```

4. Instalar dependências
```bash
pip install django whitenoise
```

5. Rodar migrações
```bash
python manage.py migrate
```

6. Criar superusuário
```bash
python manage.py createsuperuser
```

7. Rodar o servidor
```bash
python manage.py runserver
```

Acesse:
```bash
http://127.0.0.1:8000/
```

## IMAGENS (IMPORTANTE)
Imagens de categorias e produtos são salvas em:
```bash
/media/
```

Certifique-se de que:
A pasta 
```bash
media/
```
 existe
As imagens foram enviadas corretamente via admin

## LOGIN

Acesse:

```bash
/login/
```

Use o usuário criado com createsuperuser

ROTAS PRINCIPAIS
```
/ → Home
/cardapio/ → Lista de produtos
/informacoes/ → Informações da loja
/lista/ → Lista de desejos
/login/ → Login
/logout/ → Logout
```

## COMO EDITAR O PROJETO
### 1. Alterar layout 

```
/ design
```

Editar:
```
static/cafeteria/style.css
```

### 2. Alterar páginas HTML

Editar:
```
templates/
```

### 3. Alterar lógica do sistema

Editar:

```
cafeteria/views.py
```

### 4. Alterar banco de dados

Editar:
```
cafeteria/models.py
```

Depois rodar:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4.Alterar rotas

Editar:
```
cafeteria/urls.py
```

## CONFIGURAÇÃO IMPORTANTE
```
Static (CSS)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
Media (imagens)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## MODO PRODUÇÃO

Para rodar com:

```
DEBUG = False
```

WhiteNoise é usado para arquivos estáticos
Media é servido manualmente via URL
TESTES RÁPIDOS
Testar CSS:

```
/static/cafeteria/style.css
```

Testar imagem:
```
/media/categorias/arquivo.jpg
```

## AUTOR

Projeto desenvolvido por Jenifer.
