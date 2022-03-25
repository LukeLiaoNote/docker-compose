# Mysql

> Description : Starting up middleware in a min.
> More info about mysql docker image refer to [mysql docker](https://hub.docker.com/_/mysql) .

### default settings

| setting | value |  
| ------- | ------ |
| mysql version | 5.7 |
| mysql port | 3306 |  
| always restart | true |
| PASSWORD[^1] | passw0rd|

`Tips`: [^1]: is the default root password set in mysql.env.  

### dependencies

- docker-compose
- docker

### Quick start

> more user guide refer to [docker](https://docs.docker.com/get-started) *AND* [docker-compose](https://docs.docker.com/compose/) .

- Start :  （启动实例）

  ```sh
  cd mysql
  docker-compose up -d
  ```

- Down : 停止并删除实例（不删除已挂载数据）

  ```sh
  cd mysql
  docker-compose down
  ```

- logs : 查看日志

  ```sh
  cd mysql
  docker-compose logs -f mysql
  ```

- exec : 进入容器console

  ```sh
  cd mysql
  docker-compose exec mysql /bin/bash
  ```
