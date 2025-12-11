# CiteSeer Sitemap Generator
Python scripts that may be used to generate a sitemap for [CiteSeerX](https://citeseerx.ist.psu.edu/)  
# Usage
Run Doi Text File generation, then run Sitemap Generation  
See example at bottom
## 1. Doi Text File Generation
**For batch creation you must have both doi_txt_maker.py and doi_txt_makerFull.py downloaded in the same work space**
### A. Single-direcotry  
```bash
python3 doi_txt_maker.py
```
This will create a single txt file holding all doi under that directory  
Usage:  
`python3 doi_txt_paker.py <repo_path> <output_directory> <$hex>`  
Repo =  directory that holds all the data to be put into the sitemap  
$hex = "ID" i.e. what to put in `DOI{$hex}.txt`  
Repo is the second level directory that holds data  
doi_txt_maker.py is meant to be repeatedtly used
```
TopLevelRepo
+-- 00
+-- 01
+-- aa
```
Targets: either 00, 01, aa
### B. Batch creation(all subdirectories)
```bash
python3 doi_txt_makerFull.py
```
This will create txt files for each top level directory under your chosen root, each txt file contains all the DOI's from everything under them  
Runs doi_txt_maker.py for each directory one level lower than the provided  
Usage:  
`python3 doi_txt_makerFull.py <repo_rath> <output_directory>`  
Repo = top level directory that holds all the data to be put into the sitemap
doi_txt_makerFull.py meant to be used once  
```
TOPLevelRepo
+-- 00
+-- 01
+-- aa
```
Target: TopLevelRepo

## 2. Sitemap Generation
Run: 
```bash
python3 sitemap_maker.py
```
Creates sitemaps and a sitemap index of those  
Sitemaps in ```./sitemaps/``` and the sitemap index will be ```./sitemap_index.xml```  
Usage: `python3 sitemap_maker.py <doiFile_directoryPath>`  
Each sitemap contains 49,999 entries, excluding the sitemap index

# Example
```
+-- Repo
    +-- 00
        +-- aa
            +-- 00aa32134f8.pdf
        +-- af
            +-- 00af47a8908.pdf
    +-- b2
        +-- 0f
            +-- b20f9b8a6f00.pdf
        +-- a4
            +-- bfa4a9ff0abb.pdf
    +-- ff
        +-- 00
            +-- ff0043322213.pdf
        +-- ff
            +-- ffff34234324.pdf
```
Run: `python3 doi_txt_maker.py Repo/00 output 00`  
Makes `DOI00.txt` in output, holds 00aa and 00af  

Run: `python3 doi_txt_makerFull.py Repo output`
creates `DOI1.txt`, `DOI2.txt`, and `DOI3.txt` in output, holds each of their respective content


Example output Dir: 
```
output
+-- DOI1.txt
+-- DOI2.txt
+-- DOI3.txt
```
Run: `python3 sitemap_maker.py output`
Result in directory holding `sitemap_maker.py` example  
```
//existed before
doi_txt_maker.py
doi_txt_makerFull.py
sitemap_maker.py
//created
allDOI.txt
sitemap_index.xml
sitemaps
+-- sitemap1.xml
+-- sitemap2.xml
+-- sitemap3.xml
```
