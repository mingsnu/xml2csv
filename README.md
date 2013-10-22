xml2csv
=======

A python script to transform xml files to one csv file.

Usage
======
In python command line:

```python
import * from xml2csv
xml2csv(inputfile,outputfile,header)
```

- inputfile: One 'xml' file or a direcotry contains 'xml' files
- outputfile: Output csv file name, if not given, 'output.csv'is created in the same level of the input directory (when inputfile is a directory) or in the parent folder ofthe input file (when inputfile is a single xml file).
- header: A logical vallue defines whether to create csv file header.
