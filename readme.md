# CiteSeer Sitemap Generator
Python scripts that may be used to generate a sitemap for [CiteSeerX](https://citeseerx.ist.psu.edu/)  
# Usage
## 1. Doi Text File Generation
### A. Single-direcotry  
```bash
python3 doi_txt_maker.py
```
This will create a single txt file holding all doi under that directory  
Promted for: 
1. Path to repositroy directory
2. Output directory
3. Name suffix: DOI(suffix).txt  

### B. Batch creation(all subdirectories)
```bash
python3 doi_txt_makerFull.py
```
This will create txt files for each top level directory under your chosen root, each txt file contains all the DOI's from everything under them  
Promted for: 
1. Top level Repo/Directory path  
2. Output location

## 2. Sitemap Generation
Run: 
```bash
python3 sitemap_maker.py
```
Creates sitemaps and a sitemap index of those  
Sitemaps in ```./sitemaps/``` and the sitemap index will be ```./sitemap_index.xml```  
Promted for: Location of DOI txt files