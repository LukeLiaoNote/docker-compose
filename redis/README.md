# Redis

> Description : Starting up middleware in a min.
> More info about redis docker image refer to [redis docker](https://hub.docker.com/_/redis) .

### default settings

| setting | value |  
| ------- | ------ |
| redis version | 5.0 |
| redis port | 6379 |  
| always restart | true |
| PASSWORD | qwer1234 |


### dependencies

- docker-compose
- docker

### Quick start

> more user guide refer to [docker](https://docs.docker.com/get-started) *AND* [docker-compose](https://docs.docker.com/compose/) .

- Start  

  ```sh
  cd redis
  docker-compose up -d
  ```

- Down

  ```sh
  cd redis
  docker-compose down
  ```

- logs

  ```sh
  cd redis
  docker-compose logs -f redis
  ```
