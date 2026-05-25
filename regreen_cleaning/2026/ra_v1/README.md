### 1. pull & run mysql server 5.7 docker image 

```zsh
docker pull mysql:5.7

docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=your_password --rm \
  -v /Users/victor/Documents/projects/mini_projects/regreen_cleaning/2026/ra_v1/somalia:/var/lib/mysql-files \
  -p 3306:3306 -d mysql:5.7

#verify container is running
docker ps
```

### 2. Connect to the MySQL container:
use a MySQL client,  or 

in cli
```zsh
mysql -h 127.0.0.1 -P 3306 -u root -p
```
create the db:
```sql
create database ra_db_2024;
```

### 3. Restore the db
exit server instance >> in terminal(where `[backup_file].sql` lives), 
```zsh
mysql -h 127.0.0.1 -P 3306 -u root -p ra_db_2024 < [backup_file].sql

```
