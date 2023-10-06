import csv
import sys

def main():
    final_dict = import_csv_database("database_dummy.csv")
    print()

def import_csv_database(database):
    fieldnames = ["Film Titel", "Fede Skurke", "Bar Hud", "Vilde Våben", "One Liners", "Episk Action", "Total Score"]
    final_dict = {}
    try:
        with open(database, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for i, row in enumerate(reader):
                final_dict[i] = row
        return final_dict
    except FileNotFoundError:
        sys.exit(f"Could not read {database}.")

def sort_by_total_score():
    """"""



if __name__ =="__main__":
    main()



