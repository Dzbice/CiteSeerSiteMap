import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
import re
def txtDoi(path,index,output):
    stringBuilder = '' #predefine stringbuilder used to get all of the names for links
    expression = re.compile("0-9[a-f]{2}") 
    for root, dirs, files in os.walk(path, topdown=False):
        dirs = [d for d in dirs if expression.match(d)] #skip anything that isn't of the form of a 2 digit hex expression.
        for name in files:
            stringBuilder = stringBuilder + name[0:-4] +"\n"
    os.makedirs(output, exist_ok=True)
    with open(f"{output}/DOI{index}.txt","w")as fp:
        fp.write(stringBuilder) 
            
def combineDOi(DOIPath):
    if os.path.exists("allDOI.txt"): #re creating alldoi file
        os.remove("allDOI.txt")
    fp = open("allDOI.txt","a")  
    for file in os.listdir(DOIPath): #adding to alldoi
        with open(f"{DOIPath}/{file}","r") as read:
            for i in read:
                fp.write(i)
    fp.close()
        
def sitemaps(full_doi): 
    os.makedirs("sitemaps", exist_ok=True)
    baseUrl = "https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi="
    doi = open(full_doi,"r")
    listed = doi.readlines()
    x = 0
    y = 1

    while x <len(listed):
        root = ET.Element("urlset") 
        for i in range(1,50000): #49999 entries in each
            if(x >= len(listed)):
                break
            url = ET.SubElement(root,"url")
            loc = ET.SubElement(url,"loc")
            loc.text = baseUrl + listed[x].strip() #gets rid of whiteSpace
            x = x+1
        with open(f"sitemaps/sitemap{y}.xml","w") as f:
            f.write(minidom.parseString(ET.tostring(root, encoding="utf-8")).toprettyxml(indent="  "))
            y = y+ 1

    doi.close()

def sitemapIndex():
    baseurl = "https://citeseerx.ist.psu.edu/"
    root = ET.Element("sitemapindex")
    with os.scandir("sitemaps") as entries:
        for entry in sorted(entries, key=lambda e: e.name): #sorts entries based on name
            sitemap = ET.SubElement(root,"sitemap")
            loc = ET.SubElement(sitemap,"loc")
            loc.text = baseurl + entry.name
        with open("sitemap_index.xml","w") as f:
                f.write(minidom.parseString(ET.tostring(root, encoding="utf-8")).toprettyxml(indent="  "))


if __name__ ==  "__main__":
    print("Give repo path")
    x = input()
    print("Give output path for all the DOI files")
    y = input()
    dirs = os.listdir(x)
    dirs.sort()
    print(dirs)
    for i in range(len(dirs)):
        txtDoi(f"{x}/{dirs[i]}",i,y)
    print("Combined doi files will be output into directory of this script")
    combineDOi(y)
    sitemaps("allDOI.txt")
    sitemapIndex()

    