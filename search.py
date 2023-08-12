import sys
from csv import DictReader


class main:
    args = sys.argv[1:]
    counter = 0

    if not args[0]:
        search_input = input("Type Language Name To Search? ").lower().strip()
    else:
        search_input = args[0].lower().strip()

    with open('favorites.csv', 'r') as file:
        reader = DictReader(file)
        for row in reader:
            language = row['language'].lower().strip()

            if language == search_input:
                counter += 1

        print(f"{search_input}: {counter}")
