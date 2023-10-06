import csv
import sys

def main():
    film_titel, fede_skurke, bar_hud, vilde_våben, one_liners, episk_action, total_scare = import_csv_database(sys.argv[1])
    print(film_titel)
    print(fede_skurke.lstrip())


def import_csv_database(database):
    """Import the CSV database"""
    # Define fieldnames
    fieldnames = ["Film Titel", "Fede Skurke", "Bar Hud", "Vilde Våben", "One Liners", "Episk Action", "Total Score"]

    # Open the CSV file
    try:
        with open(database, newline='') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            film_titel, fede_skurde, bar_hud, vilde_våben, one_liners, episk_action, total_scare = sort_data(reader)
        return film_titel, fede_skurde, bar_hud, vilde_våben, one_liners, episk_action, total_scare
    # Look for the file, raaise FileNotFoundError
    except FileNotFoundError:
        sys.exit(f"Could not read {database}.")


def sort_data(reader):
    """Sort the data of the database"""
    for row in reader:
        for key in row.keys():
            row['Film Titel'] = row['Film Titel'].removeprefix('[')
            row['Total Score'] = row['Total Score'].removesuffix(']')
        return row['Film Titel'], row['Fede Skurke'], row['Bar Hud'], row['Vilde Våben'], row["One Liners"], row["Episk Action"], row['Total Score']



# def remove_suffix_prefix():
   # """Remove the suffixes and prefixes in the database"""



if __name__ =="__main__":
    main()



