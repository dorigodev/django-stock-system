[PYTHON__BADGE]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[DJANGO__BADGE]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[DOCKER__BADGE]: https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white
[POSTGRESQL__BADGE]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[HTML__BADGE]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[CSS__BADGE]:https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white



<h1 align="center" style="font-weight: bold;">Django Stock System 💻</h1>

![python][PYTHON__BADGE]
![djago][DJANGO__BADGE]
![docker][DOCKER__BADGE]
![postgresql][POSTGRESQL__BADGE]
![html][HTML__BADGE]
![css][CSS__BADGE]

<p align="center">
 <a href="#started">Getting Started</a> • 
  <a href="#routes">API Endpoints</a> •
 <a href="#colab">Collaborators</a> •
 <a href="#contribute">Contribute</a>
</p>

<p align="center">
  <b>Este projeto se refere a um sistema de estoque de produtos feito puramente em Django, para a Projeto Integrador I da Universidade Virtual do Estado de São Paulo e para treinar os conhecimentos no framework.</b>
</p>

<h2 id="started">🚀 Iniciando o projeto</h2>

Para conseguir rodar o projeto, é necessários algumas ferramentas.

<h3>Pré-requisitos</h3>

Para rodar o projeto é necessário ter em seu computador:

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

<h3>Clone o repositório</h3>


```bash
git clone https://github.com/dorigodev/django-stock-system
```

<h3> Environment Variables</h2>

entre na pasta `dotenv_files`, crie o arquivo `.env` seguindo o exemplo que já temos em `.env-example`, ou copie abaixo.

Dica: para a criação da `SECRET_KEY`, utilize o [Djecrety](https://djecrety.ir/) 

```yaml
SECRET_KEY="CHANGE-ME"

# 0 False, 1 True
DEBUG="1"

# Comma Separated values
ALLOWED_HOSTS="127.0.0.1, localhost"

DB_ENGINE="django.db.backends.postgresql"
POSTGRES_DB="CHANGE-ME"
POSTGRES_USER="CHANGE-ME"
POSTGRES_PASSWORD="CHANGE-ME"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"
```

<h3>Iniciando o projeto</h3>

Para iniciar o projeto, siga o passo a passo!

```bash
cd django-stock-system
docker-compose build
docker-compose up
``````


<h2 id="colab">🤝 Colaboradores </h2>

Um muito obrigado a todos que colaboraram nesse projeto!

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/dorigodev">
        <img src="https://avatars.githubusercontent.com/u/98785845?v=4" width="100px;" alt="Fernanda Kipper Profile Picture"/><br>
        <sub>
          <b>Murilo Dorigo</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="https://github.com/rillarydev">
        <img src="https://avatars.githubusercontent.com/u/94876655?v=4" width="100px;" alt="Fernanda Kipper Profile Picture"/><br>
        <sub>
          <b>Rillary Ferreira</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

