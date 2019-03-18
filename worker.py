previous_number = None


def preload():
    print("Running preload")


def cleanup():
    pass


def run(task):
    global previous_number
    previous_number = task
    print("Current Num : " + str(task))
