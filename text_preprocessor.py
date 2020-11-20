from os import sys 
import re 

def process_file(filename, outfile):
    with open(filename) as mdFile, open(outfile, 'w') as process_doc:
        lines = mdFile.readlines()
        for line in lines:
            process_doc.write('-> ' + line)


def preprocessor(line):
    if re.search()

if __name__=="__main__":
    process_file("README.md", "README_process.md")

