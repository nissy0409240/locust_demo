from locust import HttpUser, TaskSet, task, between


class WebsiteTasks(TaskSet):
    
    @task(1)
    def index(self):
        self.client.get('/')
        

class WebsiteUser(HttpUser):
    tasks = {WebsiteTasks:1}
    wait_time = between(5, 15)

