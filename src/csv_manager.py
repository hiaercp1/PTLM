import csv
import os
from rich.console import Console
from rich.table import Table

DIR = "./TODO_CSV/"

def check_csv_file():

    if not os.path.exists(DIR):

        answer = None

        while answer not in ["y","n"]:

            answer = input("Error: The program needs a TODO_CSV directory in order to function properly, should we create the directory right now to continue? [y/n] ")

        if answer == "n":

            print("Please create the needed directory.")
            exit()

        else:

            os.makedirs("TODO_CSV")
            print("Directory TODO_CSV created successfully.")

    file_count = 0
    csv_files = []

    for file in os.listdir(DIR):

        if file.endswith(".csv"):

            csv_files.append(file)
            file_count += 1

    if file_count == 0:

        answer = None

        while answer not in ["y","n"]:

            answer = input("Error: The program needs a csv files to store your tasks, should we create the csv file right now to continue? [y/n] ")

        if answer == "n":

            print("Please create the needed file.")
            exit()

        else:

            file = open("./TODO_CSV/TODO.csv", "w")
            file.write("")
            file.close()
            print("File TODO.csv created successfully.")

            return "TODO.csv"

    elif file_count > 1:

        answer = None
        while answer not in csv_files:
            answer = input("Error: More than one scv file detected, which one do you want to use? ")

        return answer

    else:
        return csv_files[0]

def write_entry(filename, items_tba):

    with open(DIR+filename, "a") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(items_tba)

def remove_entry(filename,ID):

    with open(DIR+filename,"r") as csv_file:

        rows = list(csv.reader(csv_file))

        for row in rows:

            if row[0] == ID:
                rows.pop(rows.index(row))

    with open(DIR+filename,"w") as csv_file_write:

        writer = csv.writer(csv_file_write)
        writer.writerows(rows)

def check_entry(filename,argument):

    rows = []
    row = []

    with open(DIR+filename,"r") as csv_file:

        if argument == "all":

            for line in csv.reader(csv_file):

                for x in line:

                    row.append(x)

                rows.append(row)
                row = []

        else:

            file_rows = list(csv.reader(csv_file))

            for line in file_rows:

                if line[0] == argument:

                    for i in line:
                        row.append(i)

                    rows.append(row)

        if rows == []:

            print(f"Error: There is no entry with specified ID: {argument}")
            exit()

        t = Table(title="PTLM")

        columns = ["ID","X","Priority","Note","Done"]

        for column in columns:
            t.add_column(column)

        for row in rows:
            t.add_row(*row, style="red")

        console = Console()
        console.print(t)

def modify_entry(filename,modify_list):

    id_to_modify = modify_list[0]

    if modify_list[2].lower() not in ["low","medium","high","critical","-"] or modify_list[4] not in ["True","False","-"]:

        print("Error: unsupported values.")
        exit()

    modify_list.pop(0)

    with open(DIR+filename,"r") as csv_file:

        reader = csv.reader(csv_file)
        rows = list(reader)

        for row in rows:

            if row[0] == id_to_modify:

                for c in modify_list:

                    if c == "-":
                        continue

                    row[modify_list.index(c)+1] = c

    with open(DIR+filename,"w") as csv_file_write:

        writer = csv.writer(csv_file_write)
        writer.writerows(rows)

def clear_file(filename):

    file = open(filename,"w")
    file.write("")
    file.close()
