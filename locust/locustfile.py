import os

from locust import TaskSet, task, HttpUser, between

QUIET_MODE = True if os.getenv("QUIET_MODE", "true").lower() in [
    '1', 'true', 'yes'] else False
# TASK_DELAY_FROM = int(os.getenv("TASK_DELAY", "5"))
# TASK_DELAY_TO = int(os.getenv("TASK_DELAY", "30"))


def log(message):
    if not QUIET_MODE:
        print(message)


class TestBehaviour(TaskSet):
    @task(1)
    def task1(self):
        log("running task1")
        self.client.get("/")

    @task(2)
    def task2(self):
        log("running task2")
        self.client.get("/?p=1")

    @task(2)
    def task3(self):
        log("running task3")
        self.client.get("/?p=8")

    @task(2)
    def task4(self):
        log("running task4")
        self.client.get("/?p=10")


class TestUser(HttpUser):
    tasks = [TestBehaviour]
    # wait between 5 and 30 seconds
    wait_time = between(1, 2)
