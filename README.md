# Hummingbird Cloud
---
#### Materia: Desarrollo de Aplicaciones en la Nube

##### Campus: CSF

##### Integrantes:
1. Antony Adrian Morales Rosas A01019582
2. Santa Esmeralda Magdaleno Morales A01023086

---
## 1. Aspectos generales

### 1.1 Requerimientos técnicos

A continuación se mencionan los requerimientos técnicos mínimos del proyecto, favor de tenerlos presente para que cumpla con todos.

* El equipo tiene la libertad de elegir las tecnologías de desarrollo a utilizar en el proyecto, sin embargo, debe tener presente que la solución final se deberá ejecutar en una de las siguientes plataformas en la nube: [Google Cloud Platform](https://cloud.google.com/?hl=es), [Amazon Web Services](https://aws.amazon.com/) o [Microsoft Azure](https://azure.microsoft.com/es-mx/).
* El proyecto deberá utilizar 
* La solución debe utilizar una arquitectura de microservicios. Si no tiene conocimiento sobre este tema, le recomendamos la lectura [*Microservices*](https://martinfowler.com/articles/microservices.html) de [Martin Fowler](https://martinfowler.com).
* La arquitectura debe ser modular, escalable, con redundancia y alta disponibilidad.
* La arquitectura deberá estar separada claramente por capas (*frontend*, *backend*, *API RESTful*, datos y almacenamiento).
* Deberá utilizarse contenedores [Docker](https://www.docker.com/) y un orquestador como [Kubernetes](https://kubernetes.io/).
* La API deberá utilizar autenticación y estar desplegada detrás de un API Manager como [Cloud Endpoints](https://cloud.google.com/endpoints/).
* El proyecto deberá contar con los archivos de configuración y *scripts* necesarios para crear toda la infraestructura necesaria, utilizando alguna solución de *Infraestructure as a Code* como [Deployment Manager](https://cloud.google.com/deployment-manager/).
* Todo el código, *datasets* y la documentación del proyecto debe alojarse en este repositorio de GitHub. Favor de mantener la estructura de carpetas propuesta.

### 1.2 Estructura del repositorio
El proyecto debe seguir la siguiente estructura de carpetas, la cual generamos por usted:
```
- / 			        # Raíz de todo el proyecto
    - README.md			# Archivo con los datos del proyecto (este archivo)
    - frontend			# Carpeta con la solución del frontend (Web app)
    - backend			  # Carpeta con la solución del backend (CMS)
    - api			      # Carpeta con la solución de la API
    - datasets		  # Carpeta con los datasets y recursos utilizados (csv, json, audio, videos, entre otros)
    - dbs			      # Carpeta con los modelos, catálogos y scripts necesarios para generar las bases de datos
    - models			  # Carpeta donde se almacenarán los modelos de Machine Learning ya entrenados
    - docs			    # Carpeta con la documentación del proyecto
```

### 1.3 Documentación  del proyecto

Como parte de la entrega final del proyecto, se debe incluir la siguiente información:

* Descripción del problema a resolver.
* Diagrama con la arquitectura de la solución.
* Descripción de cada uno de los componentes de la arquitectura.
* Justificación de los componentes seleccionados.
* Explicación del flujo de información en la arquitectura.
* Descripción de las fuentes de información utilizadas (archivos CSV, JSON, TXT, bases de datos, entre otras).
* Guía de configuración, instalación y despliegue de la solución en la plataforma en la nube seleccionada.
* Documentación de la API. Puede ver un ejemplo en [Swagger](https://swagger.io/). 
* El código debe estar documentado siguiendo los estándares definidos para el lenguaje de programación seleccionado.

## 2. Descripción del proyecto

Las redes sociales son una parte indispensable de nuestro día a día. Nos permiten una mayor facilidad y velocidad para interconectarnos con las personas. Sin embargo, suelen estar tan presentes en nuestra vida diaria que muchas veces pasamos por alto la complejidad que tiene por detrás. Por esto mismo, en este proyecto se pretende crear las bases de una Red social que ofrece un servicio de microblogging. Este permitirá a los usuarios realizar y recibir mensajes breves a tráves de la plataforma, algo similar a Twitter.

## 3. Solución

A continuación aparecen descritos los diferentes elementos que forman parte de la solución del proyecto.

### 3.1 Arquitectura de la solución
Diagrama de Arquitectura
![Diagrama de Arquitectura](/diagrama1.png)

Diagrama del flujo del deployment
![Diagrama Flujo del Deployment](/diagrama2.png)


### 3.2 Descripción de los componentes
```
Cloud Source Repositories: Used to link the git repository to the gcp console, in order to hace CI
Cloud Build: Used to make build triggers for the Dockerfiles in the git repository 
Container Registry: Make images built from the Cloud Build to create the following services:
    -API Users: microservice for the management of the Users
    -API Posts: microservice for the manegemnt of the Posts in the app
    -Cluster Neo4j: microservice for the management of the database
    -Frontend: microservice for the frontend application
Kubernetes Engine: Used to manage the containers in a cluster, the deployment and the services.

```

### 3.3 Modelos de bases de datos utilizados
Se utilizaron las siguientes bases de datos:

- Neo4j: Al querer copiar una red social, haremos uso de neo4j dado que es una base de datos orientada a grafos. De esta manera podemos simular las relaciones entre las personas y los posts y facilitar el manejo de dichas conexiones. Además, es posible que las conexiones estén en constante movimiento, por lo que neo4j nos brindará una gran versatilidad en el manejo de la información. Además, es fácil de escalar y no disminuye su rendimiento a pesar de las cantidades enormes de nodos que puede almacenar,lo cual es extremadamente necesario para una red social.
- Redis: Redis nos permite usar la memoria en caché. A la hora que nuestra aplicación comenzará a obtener las peticiones de los datos, se creará una llave única de redis. De esta manera, la próxima vez que se requiera hacer uso de la información, redis ya contendrá una referencia a los datos de neo4j, permitiendo que nuestra aplicación sea mucho más rápida.

Más información disponible en: [README DBMS](./dbs/README.md)


### 3.4 Frontend

El Frontend fue desarrollado en Angular, esto porque necesitabamos una solución en la que pudieramos crear componentes que interactuen entre ellos.

#### 3.4.1 Lenguaje de programación
[Javascript](https://developer.mozilla.org/es/docs/Web/JavaScript)
#### 3.4.2 Framework
[Angular](https://github.com/angular/angular-cli). 
#### 3.4.3 Librerías de funciones o dependencias
[NodeJs](https://nodejs.org/es/)

### 3.5 API

*[Incluya aquí una explicación de la solución utilizada para implementar la API del proyecto. No olvide incluir las ligas o referencias donde se puede encontrar información de los lenguajes de programación, frameworks y librerías utilizadas.]*

#### 3.5.1 Lenguaje de programación
[Javascript](https://developer.mozilla.org/es/docs/Web/JavaScript)
#### 3.5.2 Framework
[Express](https://expressjs.com/es/)
[NodeJs](https://nodejs.org/es/)
[Python Flask](http://flask.pocoo.org/)
#### 3.5.3 Librerías de funciones o dependencias

Documentación Endpoints:
[users](https://github.com/tec-csf/TC3059-PF-Otono-2019-equipo-rojo/tree/master/api/users)
[posts](https://github.com/tec-csf/TC3059-PF-Otono-2019-equipo-rojo/tree/master/api/posts)

* **Descripción**:
* **URL**:
* **Verbos HTTP**:
* **Headers**:
* **Formato JSON del cuerpo de la solicitud**: 
* **Formato JSON de la respuesta**:


## 3.6 Pasos a seguir para utilizar el proyecto

*[Incluya aquí una guía paso a paso para poder utilizar el proyecto, desde la clonación de este repositorio hasta el despliegue de la solución en una plataforma en la nube.]*

### Prerequisitos:

[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

[Cuenta de GCP](https://console.cloud.google.com)

### Clonar el repositorio:

```
git clone [repository url]
```
### Abrir la consola de GCP 

### Conectar el repositorio a Cloud Source Repositories
[Getting started](https://cloud.google.com/source-repositories/docs/quickstart?hl=es&_ga=2.230610716.-1876654194.1573748571)

### Crear los triggers en Cloud Build añadiendo la ruta hacia el archivo Dockerfile que se quiere desplegar dentro del repositorio
![Cloud Build](/CloudBuild.png)

### Crear un cluster en GKE (Google Kubernetes Engine)

### Ir a Container Registry y desplegar la imagen a GKE 
![Cloud Build](/ContainerRegistry.png)

Dentro de GKE es necesario exponer los Workloads para que puedan comuncarse entre ellos
Una vez expuestos se crean automaticamente en la sección de Services & Ingress 

![Cloud Build](/GKE.png)

Se crea un Endpoint donde estan desplegados nuestros servicios

## 4. Referencias
[Microservices Article](https://medium.com/codable/microservices-devops-experience-in-the-google-cloud-platform-2bb7527bc555)

