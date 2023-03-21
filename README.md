# :purple_heart: _*Streamteco list*_ - Djavue :purple_heart:

## Projeto utilizando o vue-cli para uma aplicação web full-stack usando Django e Vue.js - Djavue.

O projeto atual trata-se de um To Do List, com o CRUD (Create, Read, Update, Delete) implementados e informações sendo salvas no banco. A ideia e atualizações futuras nesse trabalho, darão origem a um To Do Lis de filmes e séries assistidas (o STREAMTECO LIST), onde será possível, com a API de filmes, você pesquisar o título de um filme e movê-lo para um roll de filmes e séries já assistidos, ainda não assistidos, além de ser possível favoritar e dar like e deslike. 

# Segue o MVP:

## :purple_circle: Home Page
![homedjavue](https://user-images.githubusercontent.com/103264347/218226126-0f0796db-64f2-4542-82b3-1fba91d55f84.png)

## :purple_circle: Login
![logindjavue](https://user-images.githubusercontent.com/103264347/218227103-ec0ef573-6b71-4597-a95d-6dada68940b3.png)

## :purple_circle: Tasks - Tema light
![tasksdjavue](https://user-images.githubusercontent.com/103264347/218227330-1433fee8-bf0e-430e-ba68-eed652416941.png)

# Setup do Projeto 🛠️

### Passo 1

```
$ cd mytodolist
# Para criar os containers
$ docker compose build
# Para iniciar os containers
$ docker compose up -d backend frontend

# Entrando no container backend 
$ docker-compose exec backend ./manage.py createsuperuser
```

### Passo 2

Para preparar o ambiente para que seja possível evoluir o frontend, dado que algumas pastas foram geradas pelo processo de build do docker, vamos precisar fazer alguns ajustes:

```
# Mudar o dono da pasta de root para o seu usuário
$ sudo chown 1000:1000 -Rf frontend/
$ cd frontend
$ npm install

# Para garantir que tudo está funcionando, o comando abaixo tem que rodar sem dar erro:
$ npm run lint
  > frontend@1.0.0 lint /home/user1/workspace/mytodolist/frontend
  > npm run lint:js
  > frontend@1.0.0 lint:js /home/user1/workspace/mytodolist/frontend
  > eslint --ext ".js,.vue" --ignore-path .gitignore .

```


```
# Para parar todos os containers
$ docker-compose down
```

Para acessar os serviços, utilize as URLs abaixo:

- `http://localhost` para acessar o frontend
- `http://localhost/api` para acessar diretamente alguma rota da API MOCK