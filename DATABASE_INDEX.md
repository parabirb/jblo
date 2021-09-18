# Database List
This list contains every database driver officially supported by the jblo team.

## MongoDB
MongoDB is the main database jblo supports. The MongoDB driver does not require write access and can be ran without it. The MongoDB driver config has three parameters:
* MongoDB URL (this is the URL of your MongoDB instance with authentication)
* Database Name (this is the name of the database you're using)
* Collection Name (this is the name of the collection you're using)

That's all there is to using it! When you run `node config-gen`, The MongoDB driver should be the first option in the list. Just enter `0` to use it.
## JSON (planned)
JSON is an upcoming driver which literally just uses a JSON file as the database. This is perfectly fine for most users. There is only one parameter:
* File Name (this is where your database will be stored)
## Loki (planned)
Loki is an upcoming driver which will use LokiJS as its database. Loki runs pretty fast and still saves to a file. There is only one parameter:
* File Name (this is where your database will be stored)