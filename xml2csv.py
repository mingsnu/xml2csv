#!/usr/bin/python
from bs4 import BeautifulSoup
import os
import sys

"""
List all of the files in the current directory and sub-directories.
"""

def list_all_files(inputDir):
    allFiles = []
    for (dirname, dirnames, filenames) in os.walk(inputDir):
        # Put all file names end up with ".xml" in the input dictionary to a list
        allFiles = allFiles + [os.path.join(dirname,filename) for filename in filenames if filename.endswith(".xml")]
    return(allFiles)

"""
If the output direcotry does not exist, make one.
"""

def ensure_output_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

"""
inputfile: One 'xml' file or a direcotry contains 'xml' files
outputfile: Output csv file name, if not given 'output.csv'is created
in the same level of the input directory (when inputfile is a directory) or in the parent folder of
the input file (when inputfile is a single xml file).
header: A logical vallue defines whether to create csv file header.
"""
def xml2csv(inputfile, outputfile=None, header=False):
    ## If the inputfile is a direcotry
    if os.path.isdir(inputfile):
    ## If outputfile is not given, set it to 'output.csv' in the same
    ## directory with the inputfile
        if outputfile is None:
            outputfile = os.path.abspath(os.path.join(inputfile, "..", "output.csv"))
        else:
            ensure_output_dir(outputfile)
        inputfiles = list_all_files(inputfile)
        with open(outputfile, 'a') as outf:
            ## print header
            if header:
                with open(inputfiles[0], 'r') as f:
                    soup = BeautifulSoup(f)
                    taglist=[tag.name if tag.string is not None else 'None' for tag in soup.find("nhtsa").find_all()]
                    outf.write(",".join(taglist) + "\n")
            ## print cases
            for inputfile in inputfiles:
                with open(inputfile, 'r') as f:
                    soup = BeautifulSoup(f)
                    itemlist=[tag.string if tag.string is not None else 'None' for tag in soup.find("nhtsa").find_all()]
                    outf.write(",".join(itemlist) + "\n")
    ## If the inputfile is a file
    else:
        if outputfile is None:
            outputfile = os.path.abspath(os.path.join(os.path.dirname(inputfile), "..", "output.csv"))
        else:
            ensure_output_dir(outputfile)

        with open(outputfile, 'a') as outf:
            with open(inputfile, 'r') as f:
                soup = BeautifulSoup(f)
                if header:
                    taglist=[tag.name if tag.string is not None else 'None' for tag in soup.find("nhtsa").find_all()]
                    outf.write(",".join(taglist) + "\n")
                itemlist=[tag.string if tag.string is not None else 'None' for tag in soup.find("nhtsa").find_all()]
                outf.write(",".join(itemlist) + "\n")
        
if __name__ == "__main__":
    xml2csv(unicode(sys.argv[1]))
