import logging
import os

from locust import TaskSet, task, HttpUser, between, events

QUIET_MODE = True if os.getenv("QUIET_MODE", "true").lower() in [
    '1', 'true', 'yes'] else False
TASK_DELAY_FROM = int(os.getenv("TASK_DELAY", "5"))
TASK_DELAY_TO = int(os.getenv("TASK_DELAY", "30"))


# TIME_LIMIT = 60
# SPAWN_RATE = 20


def log(message):
    if not QUIET_MODE:
        print(message)


class TestBehaviour(TaskSet):

    # @task(1)
    # def task1(self):
    #     log("running task1")
    #     self.client.get("/")

    # @task(2)
    # def task2(self):
    #     log("running task2 - Blog post com uma imagem de aproximadamente 1mb")
    #     self.client.get("/?p=1")

    # @task(2)
    # def task3(self):
    #     log("running task3 - Blog post com um texto de aproximadamente 400kb")
    #     self.client.get("/?p=8")

    @task(2)
    def task4(self):
        log("running task4 - Blog post com uma imagem de 300kb")
        self.client.get("/?p=1")


class TestUser(HttpUser):
    tasks = [TestBehaviour]
    # wait between 5 and 30 seconds
    wait_time = between(TASK_DELAY_FROM, TASK_DELAY_TO)


# class StagesShape(LoadTestShape):

#     stages = [
#         {"duration": 60, "users": 10, "spawn_rate": 10},
#         # {"duration": 120, "users": 100, "spawn_rate": 10},
#         # {"duration": 240, "users": 1000, "spawn_rate": 50},
#     ]

#     def tick(self):
#         run_time = self.get_run_time()

#         for stage in self.stages:
#             if run_time < stage["duration"]:
#                 tick_data = (stage["users"], stage["spawn_rate"])
#                 return tick_data

#         return None


# @events.test_start.add_listener
# def on_test_start(**kwargs):
#     print("A new test is starting")


# @events.test_stop.add_listener
# def on_test_stop(**kwargs):
#     print("A new test is ending")

# @events.quitting.add_listener
# def _(environment, **kw):
#     if environment.stats.total.fail_ratio > 0.01:
#         logging.error("Test failed due to failure ratio > 1%")
#         environment.process_exit_code = 1
#     elif environment.stats.total.avg_response_time > 200:
#         logging.error(
#             "Test failed due to average response time ratio > 200 ms")
#         environment.process_exit_code = 1
#     elif environment.stats.total.get_response_time_percentile(0.95) > 800:
#         logging.error(
#             "Test failed due to 95th percentile response time > 800 ms")
#         environment.process_exit_code = 1
#     else:
#         environment.process_exit_code = 0


# @events.init.add_listener
# def on_locust_init(environment, **_kwargs):
#     TimescaleListener(env=environment, testplan="timescale_listener_ex", target_env="myTestEnv")
