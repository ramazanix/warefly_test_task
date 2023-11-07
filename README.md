## How to run app
>To run the app you should follow this steps:
 
1. Install [**Docker**](https://docs.docker.com/get-docker/)
2. Clone repository and go to the project directory
3. Type in terminal:
```
sudo docker compose up -d && \
docker exec -i backend bash < migrations.sh
```

**Great! That's works!**
>Check [swagger of our app](http://localhost/docs)
