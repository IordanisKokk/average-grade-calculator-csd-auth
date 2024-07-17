# average-grade-calculator-csd-auth
A simple python script that will help you find your expected average grade

Just simple python, no extra dependencies needed for now. 

Currently only works with .csv files. modify the csv file with your own grades.
# Next Steps
- add functionality for .json files
- somehow group the courses by semester, so that it is easier for "users" to add their grades
- maybe add functionality to scrape students.auth with beautiful-soup
- Maybe in the future turn this into a backend server and create a front-end client for this (?)

# How to use

First you should modify the `data.csv` file, using Microsoft Excel, Google Sheets or even a text editor, to add your grades for each course. 
Then run the script and you will get the expected average grade.

run the script with the following command:
```bash
python grade_calculator.py csv data.csv
```

The script in general can be run with 
```bash
python grade_calculator.py ['csv' | 'json'] ['path/to/data/file']
```
