# Neo4j Documentation

## Crear contenedor de neo4j
`docker run --publish=7474:7474 --publish=7687:7687 -d --volume=$HOME/Desktop/neo4j/data:/data --env=NEO4J_AUTH=neo4j/querty neo4j`

## Diseño de la base de datos
### Etiquetas (case sensitive)
- `:User`
- `:Post`

### Relaciones (case sensitive)
- `:CREATED`
- `:FOLLOWS`
- `:LIKES`
- `:SHARED`

### User
    n:User{
        id: Integer, (Unique)
        username: String,
        mail: String, (Unique)
        password: String,
        name: String,
        location: String,
        description: String,
        verified: bool,
        created_at: Date,
        birthday: Date
        lang: String,
        profile_banner_url: String
        profile_image_url: String,
    }

### Post
    `n:Post{
        id: Integer, (Unique)
        text: String
        created_at: String,
    }`

### Created
    `a:User1 -
    r:CREATED{
        username1: String,  
        postid: Integer, 
        created_at: String,
    }
    -> b:Post`

### Follows
    `a:User1 -
    r:FOLLOWS{
        username1: String,  
        username2: String, 
        created_at: String,
    }
    -> b:User2`

### Likes
    `a:User1 -
    r:LIKES{
        username1: String,  
        postid: Integer, 
        created_at: String,
    }
    -> b:Post`

## Ejemplos Querys User
### Constrains para los usuarios
- `CREATE CONSTRAINT ON (user:User) ASSERT user.id IS UNIQUE;`
- `CREATE CONSTRAINT ON (user:User) ASSERT user.username IS UNIQUE;`
- `CREATE CONSTRAINT ON (user:User) ASSERT user.mail IS UNIQUE;`

### Ejemplo crear usuarios
- `CREATE (x:User {username:'antony999k',password:'qwerty',mail:'antony999k@hotmail.com',created_at:datetime('2017-03-01T05:12:19.717Z'),verified:false})`
- `CREATE (x:User {username:'itzel15',password:'asasfafas',mail:'itzel15@hotmail.com',created_at:datetime('2019-05-04T05:41:19.717Z'),verified:false})`

### Ejemplo follow
- `MATCH(n:User {username:"itzel15"}),(m:User {username:"antony999k"}) MERGE (n)-[r:FOLLOWS]->(m)`

### Ejemplo unfollow
- `MATCH (n:User {username:'antony999k'})-[r:FOLLOWS]->(m:User {username:'itzel15'}) delete(r)`

### Ejemplo followers de un usuario
- `MATCH ()-[r:FOLLOWS]->(n:User {username:'itzel15'}) RETURN count(r) as followers`

### Ejemplo a cuantos sigue un usuario
- `MATCH ()<-[r:FOLLOWS]-(n:User {username:'itzel15'}) RETURN count(r) as followers`

### Query de a quien seguir según tengan más posts
- `MATCH (a:User)-[r:CREATED]->(b:Post) RETURN a,COUNT(r) ORDER BY COUNT(r) LIMIT 5`

## Ejemplos Querys Post
### Ejemplo crear un post
- `MATCH(u:User {username:"antony999k"}) CREATE (u)-[:CREATED]->(:Post {text:"Este es mi primer post en colibrí", created_at:datetime('2019-05-04T05:41:19.717Z')})`

### Ejemplo eliminar un post
- `MATCH(u:Post) where ID(u)=30 DETACH DELETE(u)`

### Ejemplo obtener todos los post de las cuentas que sigues
- `MATCH (n:Post) WHERE ID(n) = 30 RETURN n`

### Ejemplo obtener un post por su id
- `MATCH (n:Post) WHERE ID(n) = 30 RETURN n`

### Ejemplo likear un post
- `MATCH(n:User {username:"itzel15"}),(m:Post) WHERE ID(m) = 30 MERGE (n)-[r:LIKES]->(m)`

### Ejemplo deslikear in post
- `MATCH (n:User {username:'itzel15'})-[r:LIKES]->(m:Post) WHERE ID(m) = 30 delete(r)`

### Ejemplo obtener los likes de un post
- `MATCH ()-[r:LIKES]->(n:Post) WHERE ID(n)=30 RETURN count(r) as likes`