# CSV Files Splitter with Python

## Requirements
- Python 3.9

## Usage
This python script expects 3 arguments.

1. CSV File Name to read from.
2. File Prefix for New Files.
3. Number of lines per new file.  

`python3 splitcsv.py <csv file> <new file prefix> <number of lines>`

Example using included `sample.csv`:  
`python3 splitcsv.py sample.csv sampleprefix 1`

Results:  

```
❯ python splitcsv.py sample.csv sampleprefix 1
[['header1', 'header2', 'header3'], ['1', '2', '3']]
[['header1', 'header2', 'header3'], ['4', '5', '6']]
[['header1', 'header2', 'header3'], ['7', '8', '9']]
[['header1', 'header2', 'header3'], ['10', '11', '12']]
[['header1', 'header2', 'header3'], ['13', '14', '15']]

❯ ls
README.md      
sample.csv     
sampleprefix_1 
sampleprefix_2 
sampleprefix_3 
sampleprefix_4 
sampleprefix_5 
splitcsv.py
```