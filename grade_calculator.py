import argparse
from load_data import load_data

def main():
    parser = argparse.ArgumentParser(description="Calculate the average grade from a CSV file.")
    parser.add_argument('file_type', help="Weather the program should import the data from a .csv or a .json file")
    parser.add_argument('csv_file', help="Path to the CSV file containing course grades", nargs='?', default='grades.csv')
    parser.add_argument('json_file', help="Path to the JSON file containing course grades", nargs='?', default='grades.json')
    args = parser.parse_args()
    
    courses = load_data(args)
    
    print(courses)
    
    total_ects = sum(course['ects'] for course in courses)
    weighted_sum = sum(course['ects'] * course['grade'] for course in courses)
    average_grade = weighted_sum / total_ects
    
    print(f"The average grade is: {average_grade:.2f}")
    return average_grade

if __name__ == '__main__':
    main()
    
