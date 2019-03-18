previous_number = None


def preload():
    pass


def cleanup():
    pass


def run(task):
    global previous_number
    previous_number = task
    print("Current Num : " + str(task))
