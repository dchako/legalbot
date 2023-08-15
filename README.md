# legalbot

Realizado con Djando y django-rest-framework utilizando python, docker, mysql y mucha genialidad.
## Development
Se necesita tener instalado docker.io con acceso a internet o tenes descargado las imagenes de mysql, adminer en su ultima version.
Ir al directorio dev/ y
- Run: `docker-compose up -d`
luego una vez levantado la base de datos volver al directorio raiz
- Run: `cd -`
y ejecutar para cargar las variables de entorno dependiendo de la situacion. en esta caso test.
- Run: `source dev/enter.sh`
sino prod
- Run: `source dev/enter.sh prod`
una vez realizado esto podremos ejecutar la api LEGALBOT de la siguiente manera.
- Run: `m runserver`

## Swagger docs
- /swagger/

## Required Environment Variables
- DB_USER
- DB_PASS
- DB_HOST
- DB_PORT
- DB_NAME