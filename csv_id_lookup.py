import os
import csv

def list_csv_files():
    """List all CSV files in the current directory."""
    return [file for file in os.listdir() if file.endswith('.csv')]

def select_file(files):
    """Prompt the user to select a file from a list."""
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")
    file_index = int(input("Select the file number: ")) - 1
    return files[file_index]

def select_column():
    """Prompt the user to select a column number."""
    column_number = int(input("Enter the column number for the unique identifier (1st column = 1): "))
    return column_number - 1

def read_unique_ids(filename, column):
    """Read unique IDs from the specified column in a CSV file."""
    unique_ids = set()
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                unique_ids.add(row[column])
    return unique_ids

def save_to_csv(data, filename):
    """Save a list of data to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in data:
            writer.writerow([item])

def csv_id_lookup():
    print("Listing CSV files...")
    csv_files = list_csv_files()

    print("Select the source CSV file:")
    source_file = select_file(csv_files)
    source_column = select_column()

    print("Select the comparison CSV file:")
    comparison_file = select_file(csv_files)
    comparison_column = select_column()

    source_ids = read_unique_ids(source_file, source_column)
    comparison_ids = read_unique_ids(comparison_file, comparison_column)

    matching_ids = source_ids.intersection(comparison_ids)
    non_matching_ids = source_ids.difference(comparison_ids)

    print(f"Number of matching IDs: {len(matching_ids)}")
    save_matching = input("Do you want to save the matching IDs to a CSV file? (yes/no): ")
    if save_matching.lower() == 'yes':
        save_to_csv(matching_ids, f"{source_file}_vs_{comparison_file}_matching_ids.csv")

    print(f"Number of non-matching IDs: {len(non_matching_ids)}")
    save_non_matching = input("Do you want to save the non-matching IDs to a CSV file? (yes/no): ")
    if save_non_matching.lower() == 'yes':
        save_to_csv(non_matching_ids, f"{source_file}_vs_{comparison_file}_non_matching_ids.csv")

if __name__ == "__main__":
    csv_id_lookup()
