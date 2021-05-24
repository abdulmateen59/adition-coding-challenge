docker-run-kafka:
	docker-compose up
	echo "** Containers are up and running **"

docker-producer:
	docker exec -t kafka \
	kafka-topics \
	  --bootstrap-server :9092 \
	  --create \
	  --topic mysql \
	  --partitions 1 \
	  --replication-factor 1
	chmod 777 task5.sh
	bash task5.sh

docker-consumer:
	docker exec -t kafka \
  kafka-console-consumer  \
    --bootstrap-server :9092 \
    --group abdm \
    --topic mysql

docker-stop:
	docker-compose down