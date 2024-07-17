import argparse
import csv


def get_file_type_and_name(file_type, args):
    if file_type == 'csv':
        file_path = args.csv_file
        #TODO check if file is pointing to csv file
    elif file_type == 'json':
        #TODO check if file is pointing to json file
        file_path = args.json_file 
    else:
        raise ValueError('file_type must be .json or .csv')
    return file_path

def load_data(args):
    file_type = args.file_type
    file_path = get_file_type_and_name(file_type, args)
    
    courses = []
    
    if (file_type == 'csv'):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                courses.append({
                    'course': row['Course'],
                    'ects': float(row['ECTS']),
                    'grade': float(row['Grade'])
                })
    return courses