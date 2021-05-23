#!/bin/bash
while read line
do
    echo "$line" | docker exec -i kafka \
                     kafka-console-producer \
                        --broker-list :9092 \
                        --topic mysql
done < <(tail -n +2 ../resources/mysql.csv)