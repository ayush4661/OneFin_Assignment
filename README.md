Backend Assignment

API Details:

GET https://demo.credy.in/api/v1/maya/movies/

The response is a paginated list of movies, returning 10 movies at a time:

{
    “count”: <total number of movies>,
    “next”: <link for next page, if present>,
    “previous”: <link for previous page>,
    “data”: [
        {
            “title”: <title of the movie>,
            “description”: <a description of the movie>,
            “genres”: <a comma separated list of genres, if present>,
		 “uuid”: <a unique uuid for the movie>
        },
        ...
    ]
}

Implement APIs for your web application

In your web application, you should allow users to register using a username and password, which should return a JWT token which should be used for authentication. All requests except the registration one should be authenticated. Post-registration, the user should be able to create collections and add movies to their collections, view, modify and delete them, essentially, you need to create CRUD APIs for collections. For all APIs and responses related to collections, you can create models, where all data related to those APIs are stored.

POST http://localhost:8000/register/

Request Payload:

{
    “username”: <desired username>,
    “password”: <desired password>
}

Response:

{
    “access_token”: <Access Token>
}

GET http://localhost:8000/movies/

This should return a paginated list of movies which are available. Note that this API should be actually calling the third party API. This data should not be obtained from your models/database. Sample response below:

{
    “count”: <total number of movies>,
    “next”: <link for next page, if present>,
    “previous”: <link for previous page>,
    “data”: [
        {
            “title”: <title of the movie>,
            “description”: <a description of the movie>,
            “genres”: <a comma separated list of genres, if present>,
		 “uuid”: <a unique uuid for the movie>
        },
        ...
    ]
}


GET http://localhost:8000/collection/

This should return my collection of movies and my top 3 favourite genres based on the movies across all my collections. Note that the response of this API need not include the actual movies inside the collections, there is a separate API for that purpose.

{
    “is_success”: True,
    “data”: {
        “collections”: [
            {
                “title”: “<Title of my collection>”,
                “uuid”: “<uuid of the collection name>”
                “description”: “My description of the collection.”
            },
            ...
        ],
        “favourite_genres”: “<My top 3 favorite genres based on the movies I have added in my collections>.”
    }
}

POST http://localhost:8000/collection/

This API creates a collection. The data for the movies should be saved in the database in this API.

Request payload:

{
    “title”: “<Title of the collection>”,
    “description”: “<Description of the collection>”,
    “movies”: [
        {
            “title”: <title of the movie>,
            “description”: <description of the movie>,
            “genres”: <generes>,
            “uuid”: <uuid>
        }, ...
    ]
}

Response payload:

{
    “collection_uuid”: <uuid of the collection item>
}

PUT http://localhost:8000/collection/<collection_uuid>/

This should update the movie list in the collection.

Request:

{
    “title”: <Optional updated title>,
    “description”: <Optional updated description>,
    “movies”: <Optional movie list to be updated>,
}

GET http://localhost:8000/collection/<collection_uuid>/

Response:

{
    “title”: <Title of the collection>,
    “description”: <Description of the collection>,
    “movies”: <Details of movies in my collection>
}

DELETE http://localhost:8000/collection/<collection_uuid>/

This should delete the collection.


Implement a scalable request counter middleware

Below API should return the number of requests which have been served by the server till now. Note that this should also work in a concurrent environment and should be scalable. There should be another API to reset the counter.

GET http://localhost:8000/request-count/

Response:
{
    “requests”: <number of requests served by this server till now>.
}

POST http://localhost:8000/request-count/reset/

Response:
{
    “message”: “request count reset successfully”
}



