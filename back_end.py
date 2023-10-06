import csv
import sys

def main():
    import_csv_database(sys.argv[1])

def import_csv_database(database):
    """Import the CSV database"""
    # Define fieldnames
    fieldnames = ["Film Titel", "Fede Skurke", "Bar Hud", "Vilde Våben", "One Liners", "Episk Action", "Total Score"]

    # Open the CSV file
    try:
        with open(database, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            for row in reader:
                for key in row.keys():
                    row['Film Titel'] = row['Film Titel'].removeprefix('[')
                    row['Total Score'] = row['Total Score'].removesuffix(']')
                print(row['Film Titel'], row['Total Score'])

    # Look for
    except FileNotFoundError:
        sys.exit(f"Could not read {read_file}.")

if __name__ =="__main__":
    main()



