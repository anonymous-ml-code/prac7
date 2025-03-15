import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    with open('languages.csv', 'r') as in_file:
        header = in_file.readline().strip()  # Read and ignore header
        
        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"
            language = ProgrammingLanguage(
                parts[0], 
                parts[1], 
                reflection, 
                int(parts[3]), 
                pointer_arithmetic
            )
            languages.append(language)
    
    for language in languages:
        print(language)


def using_csv():
    """Language file reader version using the csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)  # Skip header
        for row in reader:
            print(f"{row[0]} ({row[3]}) - Reflection: {row[2]}, Pointer Arithmetic: {row[4]}")


def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        fields = [field.replace(' ', '_') for field in next(reader)]  # Clean field names
        Language = namedtuple('Language', fields)
        
        for row in reader:
            lang = Language(*row)
            print(f"{lang.Language:12} | {lang.Typing:6} | "
                  f"Reflection: {lang.Reflection:3} | "
                  f"Pointer Arithmetic: {lang.Pointer_Arithmetic}")


def using_csv_namedtuple():
    """Version using both csv module and named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        fields = [field.replace(' ', '_') for field in next(reader)]
        Language = namedtuple('Language', fields)
        
        for lang in map(Language._make, reader):
            print(f"{lang.Language:15} - PA: {lang.Pointer_Arithmetic:3} ({lang.Year})")


if __name__ == "__main__":
    print("=== Standard Version ===")
    main()
    
    print("\n=== CSV Module Version ===")
    using_csv()
    
    print("\n=== Named Tuple Version ===")
    using_namedtuple()
    
    print("\n=== CSV + Named Tuple Version ===")
    using_csv_namedtuple()