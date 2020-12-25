# Ejemplo de AWS CodeBuild para construir una imagen de python-docker y subirla a AWS ECR

### Requisitos:
- Se utiliza la imagen base de docker `python:3.8.3-slim-buster`

### Deployment
- __IMPORTENTE:__ Crear el archivo **.env** se proporciona un ejemplo en **.env.example**
- En el proyecto de `AWS Codebuild` de la consola web de amazon, debido a que se usan en la ejecución de `buildspec.yaml`, es necesario configurar las siguientes variables de entorno:
    - APP_NAME (usada cuando se ejecuta el container, es necesaria para gunicorn)
    - AWS_DEFAULT_REGION
    - AWS_ACCOUNT_ID
    - ENV _(se usará para tagear a la imagen ej. latest)_
    - IMAGE_REPO_NAME

### Creación de imagen de docker local para Testing
- Para hacer build (o rebuild) de la imagen, desde la carpeta raíz del proyecto ejecutar `docker build -t docker-codebuild -f .\docker\Dockerfile .` (-t para asignar un tag a la imagen, el cual nos es muy útil para los comandos a continuación)
- El comando gunicorn en el Dockerfile conectará el puerto `0.0.0.0:8000` del container de la imagen al puerto`localhost:80` del host
- El comando `docker run --env-file ./path-to-folder-website/.env -p 80:8000 docker-codebuild:latest` crea y pone en ejecución el container de la imagen especificada en el tag (en este ejemplo se tageó a la imagen con el nombre de `docker-codebuild` que automaticamente se le tageó la versión `latest`)
- Una vez en ejecución nuestro container (podemos comprobarlo con el comando `docker ps -a` el cual nos muestra el estatus de nestros containers) revisamos su id o su nombre, con el cual podemos acceder a ciertas operaciones de él, como puede ser acceder a su bash y realizar las **migrations de django**, etc
    - **Ejemplo:** si el id del container en ejecución fuera 41985f87f328, podriamos acceder al bash (ya que el container se construyó a base de una imagen mínima de Linux, llamada alpine(Vease en el Dockerfile) y esta nos ofrece ciertas herramientas como comunicación con sh) de este con el comando `docker exec -i -t <name o id del container> bash`