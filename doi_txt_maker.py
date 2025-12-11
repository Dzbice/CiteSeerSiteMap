import os
import re
import sys




def txtDoi(path,output,index):
    os.makedirs(output, exist_ok=True)
    expression = re.compile("[0-9a-f]{2}") 
    with open(f"{output}/DOI{index}.txt","w")as fp:
        for root, dirs, files in os.walk(path, topdown=True):
            dirs[:] = [d for d in dirs if expression.match(d)] #skip anything that isn't of the form of a 2 digit hex expression.
            for _ in files:
                fp.write(f"{os.path.splitext(_)[0]}\n")


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python3 doi_txt_paker.py <repo_path> <output_directory> <$hex>")
        sys.exit()

    repo = sys.argv[1]
    outputDir = sys.argv[2]
    hex = sys.argv[3]
    txtDoi(repo,outputDir,hex)


