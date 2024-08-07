import argparse

def arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a","--add", type=str, nargs=3, help="Add an entry to the TODO list by specifying the [X] [Priority] [Note].")
    parser.add_argument("-r","--remove", type=str, nargs=1, help="Remove an entry from the TODO list by specifying the ID of that entry.")
    parser.add_argument("-c","--check", type=str, nargs=1, help="Check the status of an entry by specifying the index of that entry.")
    parser.add_argument("-m","--modify", type=str, nargs=5, help="Modify the entry in TODO list by specifying the ID of that entry.")
    parser.add_argument("-d","--done", type=str, nargs=1, help="Make the task marked as done by specifying the ID of that task.")
    parser.add_argument("-n","--nuke", type=str, nargs=1, help="Nuke the specified file.")

    return parser.parse_args()
