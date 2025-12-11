from doi_txt_maker import txtDoi
import os
import sys

if len(sys.argv) != 3:
        print("Usage: python3 doi_txt_makerFull.py <repo_rath> <output_directory>")
        sys.exit()
repo = sys.argv[1]
output = sys.argv[2]
dirs = os.listdir(repo)
dirs.sort()
for i in range(len(dirs)):
        txtDoi(f"{repo}/{dirs[i]}",output,i)