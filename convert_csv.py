import os
import csv
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def detect_delimiter(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as f:
        sniffer = csv.Sniffer()
        return sniffer.sniff(f.readline()).delimiter

def convert_csv(file_path, encoding, delimiter):
    with open(file_path, 'r', encoding=encoding) as f:
        reader = csv.reader(f, delimiter=delimiter)
        rows = list(reader)

    new_file_path = os.path.splitext(file_path)[0] + "_converted.csv"
    with open(new_file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

def main():
    csv_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]
    print("Found CSV files:", csv_files)

    for file in csv_files:
        encoding = detect_encoding(file)
        delimiter = detect_delimiter(file, encoding)
        print(f"File: {file}, Encoding: {encoding}, Delimiter: '{delimiter}'")

    choice = input("Enter file names to convert (comma-separated) or 'all' to convert all files: ").strip()
    if choice.lower() == 'all':
        files_to_convert = csv_files
    else:
        files_to_convert = [f.strip() for f in choice.split(',')]

    for file in files_to_convert:
        if file in csv_files:
            print(f"Converting {file}...")
            convert_csv(file, detect_encoding(file), detect_delimiter(file, detect_encoding(file)))
            print(f"Converted {file} to UTF-8 with comma as delimiter.")

if __name__ == "__main__":
    main()
