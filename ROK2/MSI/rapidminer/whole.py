import os
from process import process
from proccessSelection import process


if __name__ == "__main__":
    directory = "data_csv"
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        # if os.path.isfile(f):
        # process(f)

    process("./data_csv/autoMPG6.cv")
