#!/bin/bash

# --> NETWORK
docker network create -d bridge logestic-network

# --> VOLUME
docker volume create logestic-volume

# --> MySQL
docker run -d --name logestic_mysql -p 3306:3306 --network logestic-network -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=logestic -v logestic-volume:/var/lib/mysql mysql:latest

# --> PhpMyAdmin
docker run -d --name logestic-phpmyadmin -p 3307:80 --link logestic_mysql:db --network logestic-network phpmyadmin/phpmyadmin:latest

# --> logestic
docker build -t logestic:latest .
docker run -d --name logestic -p 8001:8001 -v $(pwd):/app --network logestic-network logestic
