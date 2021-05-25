run-kafka:
	docker-compose up -d
	echo "** Containers are up and running **"

create-topic:
	docker exec -t kafka \
	kafka-topics \
	  --bootstrap-server :9092 \
	  --create \
	  --topic mysql \
	  --partitions 1 \
	  --replication-factor 1

start-producer:
	chmod 777 task5.sh
	bash task5.sh

start-consumer:
	docker exec -t kafka \
  kafka-console-consumer  \
    --bootstrap-server :9092 \
    --group abdm \
    --topic mysql

stop-kafka:
	docker-compose down