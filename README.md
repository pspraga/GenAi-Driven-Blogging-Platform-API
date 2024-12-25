# GenAi-Driven-Blogging-Platform-API
Multi User Blogging
# initial setup
CHANGE database name user and password in .env file
--if not .env create manualy 
POSTGRES_DB=db name
POSTGRES_USER=username
POSTGRES_PASSWORD=password


#Docker setup and run 
Run Docker file using

1.docker-compose build
2.docker-compose down && docker-compose up --build
3.init db using docker-compose up -d
4. docker ps -a --to verifiy is the container running or exite with error
5. docker logs <container-id> to check any error on configuration
---for create super user
#.docker exec -it genai_web_1 bash
#.python3 manage.py createsuperuser.

---docker run----

you can adjust port number but here i gave 8083 for app run 

but link to view in website is http://ip or localhost:8085

/admin --for login/authenticate user
/api/articles --for article view edit add
/api/comments  --forcomment
/api/posts  --for blogpost
you can download using  http://ip or domain/swagger/ ---for view all url
