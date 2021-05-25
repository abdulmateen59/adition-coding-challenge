run-task-1-4:
	docker pull jupyter/pyspark-notebook

	docker run --user root -d --name python-spark -e CHOWN_HOME=yes -e CHOWN_HOME_OPTS='-R' -v `pwd`:/home/workspace jupyter/pyspark-notebook

	docker exec python-spark bash -c "cd /home/workspace && pip install -r requirements.txt"
	echo "\033[0;35m ***************** Task 01 *****************"
	docker exec python-spark bash -c "cd /home/workspace/Task-1 && pytest . && python task1.py"
	echo "\033[0;34m ***************** Task 02 *****************"
	docker exec python-spark bash -c "cd /home/workspace/Task-2 && pytest . && python task2.py"
	echo "\033[0;33m ***************** Task 03 *****************"
	docker exec python-spark bash -c "cd /home/workspace/Task-3 && pytest . && python task3.py"
	echo "\033[0;32m ***************** Task 04 *****************"
	docker exec python-spark bash -c "cd /home/workspace/Task-4/ && python task4.py"

	docker rm -f python-spark
