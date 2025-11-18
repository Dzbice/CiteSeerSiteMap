import xml.etree.ElementTree as ET
import os

def count_urls_in_sitemap(sitemap_path):
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    namespace = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    print(len(root.findall(namespace + 'url/' + namespace + 'loc'))) #uses xpath plus namespace to find loc elements, each representing a URL

with os.scandir("ExampleSiteMaps") as entries:
    for entry in entries:
        if entry.is_file() and entry.name.endswith('.xml'):
            print(f"Processing sitemap: {entry.name}")
            count_urls_in_sitemap(entry.path)

#49999 per file
