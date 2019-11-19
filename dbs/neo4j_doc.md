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

## Ejemplos Querys
Visita [db.cypher](./db.cypher) para ver los ejemplos del queries

## Ejemplos Relaciones
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

### Post
`n:Post{
    id: Integer, (Unique)
    text: String
    created_at: String,
}`