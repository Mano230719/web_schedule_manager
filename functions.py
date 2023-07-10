FILEPATH = "schedule.txt"


def get_schedule(filepath=FILEPATH):
    # Below is a doc-string, used like a comment to describe a certain function in the python console with "help()"
    """
    This function reads a text file and returns the list of the schedule items.
    """
    with open(filepath, "r") as file_local:
        schedule_local = file_local.readlines()
    return schedule_local


def write_schedule(schedule_arg, filepath=FILEPATH):
    """ Write the schedule list in a text file. """
    with open(filepath, "w") as file_local:
        file_local.writelines(schedule_arg)
