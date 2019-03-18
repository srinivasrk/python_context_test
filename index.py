import random
import worker_runner

tasks = []

for i in range(100):
    tasks.append(random.randint(1, 100))

worker_runner.init(tasks)