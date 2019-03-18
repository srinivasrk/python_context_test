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
        # if task is even and previous context was even then dont run preload
        # if the previous context was different then run preload
        if previous_context is not None:
            # check if previous number was even or odd
            if task % 2 == 0 and previous_context.previous_number % 2 == 0:
                # Previous context can be retained
                entry_point_runner = load_dynamic_module("entry-point", "./worker.py")
                entry_point_runner.run(task)
                entry_point_runner.cleanup()
            elif task % 2 != 0 and previous_context.previous_number % 2 != 0:
                # Previous context can be retained
                entry_point_runner = load_dynamic_module("entry-point", "./worker.py")
                entry_point_runner.run(task)
                entry_point_runner.cleanup()
            else:
                # Previous context cannot be retained
                entry_point_runner = load_dynamic_module("entry-point", "./worker.py")
                entry_point_runner.preload()
                entry_point_runner.run(task)
                entry_point_runner.cleanup()

        else:
            entry_point_runner = load_dynamic_module("entry-point", "./worker.py")
            entry_point_runner.run(task)