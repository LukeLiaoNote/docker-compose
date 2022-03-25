# Kafka

> Description : Starting up middleware in a min.
> More info about kafka  docker image refer to [kafka docker](https://hub.docker.com/r/wurstmeister/kafka) .

### default settings

| setting | value |  
| ------- | ------ |
| zookeeper version | 3.5.6 |
| zookeeper port | 2181 |  
| always restart | true |
| kafka version | 2.1.1 |
| kafka port | 9092 |
| always restart | true |
| ADVERTISED_LISTENERS | localhost |
| LISTENERS | localhost |
>使用前需要修改kafka.env配置${localhost}为本机服务器ip.
>kafka配置文件在当前项目的config目录中

### dependencies

- docker-compose
- docker

### Quick start

> more user guide refer to [docker](https://docs.docker.com/get-started) *AND* [docker-compose](https://docs.docker.com/compose/) .
> note: For the first use, you need to change the  configuration of ${localhost} in kafka.env to host IP

- Start :  （启动实例）

  ```sh

  cd kafka
  docker-compose up -d
  ```

- Down : 停止并删除实例（不删除已挂载数据）

  ```sh
  cd kafka
  docker-compose down
  ```

- Add more brokers：

```sh
cd kafka
docker-compose scale kafka=3

```

- logs : 查看日志

  ```sh
  cd kafka
  docker-compose logs -f kafka
  ```

- exec : 进入容器console

  ```sh
  cd kafka
  docker-compose exec kafka /bin/bash
  ```
