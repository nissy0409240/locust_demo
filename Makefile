locust:
	locust -H http://localhost:8080 -f locustfile.py

api_server:
	python api_server.py
