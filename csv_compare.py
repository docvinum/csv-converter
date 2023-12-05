import os
import pandas as pd
import chardet
import csv

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def convert_csv(file_path, encoding, delimiter):
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter)
            rows = list(reader)
    except UnicodeDecodeError:
        print(f"Erreur d'encodage lors de la lecture de {file_path}. Conversion ignorée.")
        return

    new_file_path = os.path.splitext(file_path)[0] + "_converted.csv"
    with open(new_file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

def compare_csv(old_file_path, new_file_path):
    df_old = pd.read_csv(old_file_path, encoding='utf-8', sep=',')
    df_new = pd.read_csv(new_file_path, encoding='utf-8', sep=',')

    key_column = df_old.columns[0]

    removed_entries = df_old[~df_old[key_column].isin(df_new[key_column])]
    new_entries = df_new[~df_new[key_column].isin(df_old[key_column])]

    common_entries_df_old = df_old[df_old[key_column].isin(df_new[key_column])]
    common_entries_df_new = df_new[df_new[key_column].isin(df_old[key_column])]
    merged_common_entries = pd.merge(common_entries_df_old, common_entries_df_new, on=key_column, suffixes=('_old', '_new'))
    modifications = merged_common_entries[merged_common_entries.filter(like='_old').ne(merged_common_entries.filter(like='_new')).any(axis=1)]

    # Select only columns 2, 3, and 4
    return new_entries.iloc[:, 1:4], removed_entries.iloc[:, 1:4], modifications.iloc[:, 1:4]

def display_entries(entries, title):
    print(f"\n{title} (affichage des 10 premières entrées) :")
    print(entries.head(10))
    start = 10
    while start < len(entries) and input("\nAfficher 10 entrées supplémentaires ? (oui/non) ").lower() == "oui":
        print(entries.iloc[start:start+10])
        start += 10

def main():
    choice = input("Choisissez une option:\n1. Convertir les fichiers CSV\n2. Comparer deux fichiers CSV\n3. Quitter\n> ")

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
            print(f"{idx + 1}. {file}")

        file_index_old = int(input("Enter the number of the old CSV file to compare: ")) - 1
        file_index_new = int(input("Enter the number of the new CSV file to compare: ")) - 1

        old_file_path = csv_files[file_index_old]
        new_file_path = csv_files[file_index_new]

        new_entries, removed_entries, modifications = compare_csv(old_file_path, new_file_path)

        print("\nSynthèse des changements :")
        print(f"- {len(new_entries)} Nouvelles entrées")
        print(f"- {len(removed_entries)} Entrées supprimées")
        print(f"- {len(modifications)} Entrées modifiées")

        display_entries(new_entries, "Nouvelles entrées")
        display_entries(removed_entries, "Entrées supprimées")
        display_entries(modifications, "Entrées modifiées")

    elif choice == "3":
        return

if __name__ == "__main__":
    main()
