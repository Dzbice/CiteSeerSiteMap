import os
import re
import time




def txtDoi(path,output,index):
    start = time.time()
    os.makedirs(output, exist_ok=True)
    expression = re.compile("[0-9a-f]{2}") 
    with open(f"{output}/DOI{index}.txt","w")as fp:
        for root, dirs, files in os.walk(path, topdown=True):
            dirs[:] = [d for d in dirs if expression.match(d)] #skip anything that isn't of the form of a 2 digit hex expression.
            for _ in files:
                fp.write(f"{os.path.splitext(_)[0]}\n")
    end = time.time()
    print(f"txtDOi time {end-start}")


if __name__ == "__main__":
    path = input("Repo Path: ")
    output = input("Output location: ")
    index =  input("name will be DOI(input).txt: ")
    txtDoi(path,output,index)


