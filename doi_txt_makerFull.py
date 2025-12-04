from doi_txt_maker import txtDoi
import time
import os

print("Give repo path")
x = input()
print("Give output path for all the DOI files")
y = input()
start = time.time()
dirs = os.listdir(x)
dirs.sort()
for i in range(len(dirs)):
        txtDoi(f"{x}/{dirs[i]}",y,i)
        print(i)
end =time.time()
print(f"total time {end-start}")


# autogenerate citations for website 
# stores authores names in database
# use firebase to store data via database
# pull from database to create citations