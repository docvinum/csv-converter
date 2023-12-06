import os
import pandas as pd
import chardet
import csv

def detect_encoding(file_path):
    """Detect the encoding of a file."""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def convert_csv(file_path, encoding, delimiter):
    """Convert a CSV file to UTF-8 encoding with a specified delimiter."""
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter)
            rows = list(reader)
    except UnicodeDecodeError:
        print(f"Encoding error when reading {file_path}. Conversion skipped.")
        return

    new_file_path = os.path.splitext(file_path)[0] + "_converted.csv"
    with open(new_file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

def compare_csv(old_file_path, new_file_path, key_column):
    """Compare two CSV files and return new, deleted, and modified entries."""
    df_old = pd.read_csv(old_file_path, encoding='utf-8', sep=',', dtype=str)
    df_new = pd.read_csv(new_file_path, encoding='utf-8', sep=',', dtype=str)

    if isinstance(key_column, int):
        key_column = df_old.columns[key_column]

    removed_entries = df_old[~df_old[key_column].isin(df_new[key_column])]
    new_entries = df_new[~df_new[key_column].isin(df_old[key_column])]

    common_entries_df_old = df_old[df_old[key_column].isin(df_new[key_column])]
    common_entries_df_new = df_new[df_new[key_column].isin(df_old[key_column])]
    merged_common_entries = pd.merge(common_entries_df_old, common_entries_df_new, on=key_column, suffixes=('_old', '_new'))
    modifications = merged_common_entries[merged_common_entries.filter(like='_old').ne(merged_common_entries.filter(like='_new')).any(axis=1)]

    return new_entries, removed_entries, modifications

def save_results_to_csv(new_entries, removed_entries, modifications, old_file, new_file):
    """Save the comparison results to CSV files."""
    new_entries.to_csv(f"{old_file}_vs_{new_file}_new_entries.csv", index=False)
    removed_entries.to_csv(f"{old_file}_vs_{new_file}_deleted_entries.csv", index=False)
    modifications.to_csv(f"{old_file}_vs_{new_file}_modified_entries.csv", index=False)

def main():
    choice = input("Choose an option:\n1. Convert CSV files\n2. Compare two CSV files\n3. Exit\n> ")

    if choice == "1":
        csv_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]
        print("Available CSV files:")
        for idx, file in enumerate(csv_files):
            print(f"{idx + 1}. {file}")

        file_index = int(input("Enter the number of the CSV file to convert: ")) - 1
        file_path = csv_files[file_index]
        encoding = detect_encoding(file_path)
        delimiter = input(f"Enter the delimiter for {file_path}: ")
        convert_csv(file_path, encoding, delimiter)
        print(f"Converted {file_path} to UTF-8 with '{delimiter}' as delimiter.")

    elif choice == "2":
        # Comparison logic
        csv_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]
        print("Available CSV files:")
        for idx, file in enumerate(csv_files):
            line_count = sum(1 for line in open(file, 'r', encoding=detect_encoding(file)))
            print(f"{idx + 1}. {file} - {line_count} lines")

        file_index_old = int(input("Enter the number of the old CSV file to compare: ")) - 1
        file_index_new = int(input("Enter the number of the new CSV file to compare: ")) - 1

        old_file_path = csv_files[file_index_old]
        new_file_path = csv_files[file_index_new]

        key_column_input = input("Enter the column name or index to use as the key for comparison: ")
        try:
            key_column = int(key_column_input) if key_column_input.isdigit() else key_column_input
        except ValueError:
            print("Invalid column index. Using the first column as default.")
            key_column = 0

        new_entries, removed_entries, modifications = compare_csv(old_file_path, new_file_path, key_column)

        print(f"\nChanges summary:")
        print(f"- {len(new_entries)} New entries")
        print(f"- {len(removed_entries)} Deleted entries")
        print(f"- {len(modifications)} Modified entries")

        if input("Do you want to save these results to CSV files? (yes/no) ").lower() == "yes":
            save_results_to_csv(new_entries, removed_entries, modifications, os.path.splitext(old_file_path)[0], os.path.splitext(new_file_path)[0])
            print("Results saved to CSV files.")

    elif choice == "3":
        return

if __name__ == "__main__":
    main()

    main()
