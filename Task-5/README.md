# Task 05
## Apache Kafka | Zookeeper | Docker Compose
Set up a single node Kafka cluster and feed it with the MySQL data from task 4. Each line 
should be a single message. Write a consumer which prints the messages you have just fed into 
Kafka to stdout.

## Make
  - Use following command to start zookeeper and kafka:
    ```sh
    $ make run-kafka
    ```
  - Create topic, default `mysql` topic name will be used:
    ```sh
    $ make create-topic
    ```
  - Start producer:
    ```sh
    $ make start-producer
    ```
  - Open new terminal , and start consumer:
    ```sh
    $ make start-consumer
    ```
  - To stop the containers use:
    ```sh
    $ make stop-kafka
    ```
---
## Built With
- Docker compose 
    - zookeeper:3.4.9
    - confluentinc/cp-kafka:5.5.1
- Bash script as a producer
- Only one Zookeeper and one Kafka are used, though it could be easily scaled.
## Getting Started
Follow step by step to setup Apache Kafka:
### Prerequisites
- docker 
- docker-compose
- Nix based OS (Not essential but tested on Debian)

### Usage

```sh
$ docker-compose up
```
- Once Kafka is up and running, leave it as is for log monitoring purpose.
- Open new terminal, and create kafka topic using following command.
```sh
$ docker exec -t kafka \
  kafka-topics \
    --bootstrap-server :9092 \
    --create \
    --topic mysql \
    --partitions 1 \
    --replication-factor 1
```
- Make sure that the topic is listed with the following command:
```sh
$ docker exec -t kafka  \
  kafka-topics \
    --bootstrap-server :9092 \
    --describe \
    --topic mysql
```

- Once the topic is created with the following command, stdout is displayed:
```sh
$ docker exec -t kafka \
  kafka-console-consumer  \
    --bootstrap-server :9092 \
    --group abdm \
    --topic mysql
```
- Now it's time for producer to feed data so we can see what's coming on the consumer side.
- Open a new terminal, run bash script using following commands: 
```sh
$ chmod 777 task5.sh
$ bash task5.sh
```
- Move back to consumer terminal to verify data feed.

## Removes containers, networks, volumes, and images created by up
```sh
$docker-compose down
```

