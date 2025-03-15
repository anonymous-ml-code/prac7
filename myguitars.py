import csv
from guitar import Guitar


def main():
    """Read guitars from file, sort them, display them, and allow adding new guitars."""
    guitars = load_guitars('guitars.csv')

    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()  # Sort guitars by year (oldest to newest)
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    add_new_guitars(guitars)

    save_guitars('guitars.csv', guitars)
    print(f"\n{len(guitars)} guitars saved to guitars.csv")


def load_guitars(filename):
    """Load guitars from the CSV file into a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r', newline='') as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars


def display_guitars(guitars):
    """Display the guitars in the list."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")


def add_new_guitars(guitars):
    """Add new guitars to the list until the user enters an empty name."""
    print("\nEnter your new guitars (or leave name blank to exit):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")


def save_guitars(filename, guitars):
    """Save the guitars to the CSV file."""
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == "__main__":
    main()
