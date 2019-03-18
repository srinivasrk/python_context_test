import importlib.util

previous_context = None


def load_dynamic_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    my_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(my_module)
    global previous_context
    previous_context = my_module
    return my_module


def init(tasks):
    for task in tasks:
        if previous_context is not None:
            print("Previous num " + str(previous_context.previous_number))
        # if task is even and previous context was even then dont run preload
        # if the previous context was different then run preload
        entry_point_runner = load_dynamic_module("entry-point", "./worker.py")
        entry_point_runner.run(task)