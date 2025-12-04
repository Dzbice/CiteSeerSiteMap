import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
import time

def combineDOi(DOIPath):
    start = time.time()
    if os.path.exists("allDOI.txt"): #re creating alldoi file
        os.remove("allDOI.txt")
    fp = open("allDOI.txt","a")  
    for file in os.listdir(DOIPath): #adding to alldoi
        with open(f"{DOIPath}/{file}","r") as read:
            for i in read:
                fp.write(i)
    fp.close()
    end = time.time()
    print(f"combineTime: {end-start}")
    return "allDOI.txt"
def sitemapGen(alldoi): #alldoi is the path to the txt file with all doi files
    start = time.time()
    os.makedirs("sitemaps", exist_ok=True)
    batch = []
    index = 1
    with open(alldoi,"r") as fp:
        for _ in fp:
            batch.append(_)
            if(len(batch) == 49999):
                xmlWrite(batch,index)
                batch =[]
                index+=1
    if batch:
        xmlWrite(batch, index)

    end = time.time()
    print(f"Sitemaps generated in {end - start:.2f} seconds")
            

def xmlWrite(batch,index):
    baseUrl = "https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi="
    root = ET.Element("urlset")
    for i in batch:
        url = ET.SubElement(root,"url")
        loc = ET.SubElement(url,"loc")
        loc.text = baseUrl + i.strip()
    with open(f"sitemaps/sitemap{index}.xml","w") as f:
        f.write(minidom.parseString(ET.tostring(root, encoding="utf-8")).toprettyxml(indent="  "))

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



DOI = input("DOi files directory path: ")
sitemapGen(combineDOi(DOI))
sitemapIndex()
    

