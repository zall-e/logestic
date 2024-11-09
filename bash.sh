#!/bin/bash

# --> NETWORK
docker network create -d bridge logestic-network

# --> VOLUME
docker volume create logestic-volume

# --> MySQL
docker run -d --name logestic_mysql -p 3306:3306 --network logestic-network -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=logestic -v logestic-volume:/var/lib/mysql mysql:latest

# --> PhpMyAdmin
docker run -d --name logestic-phpmyadmin -p 3307:80 --link logestic_mysql:db --network logestic-network phpmyadmin/phpmyadmin:latest

# # --> Padafand
# docker build -t padafand:latest .
# docker run -d --name Padafand -p 8001:8001 -v $(pwd):/app --network padafand-network padafand
