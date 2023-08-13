# using datetime module
from datetime import datetime
from csv import DictWriter

class main:

    # get values from user
    language_value = input("Language? ").strip()
    problem_value = input("Problem? ").strip()

    # List that we want to add as a new row
    fields = [
        # datetime.now().timestamp(),
        datetime.now(),
        language_value,
        problem_value
    ]

    # List of fields [column]
    fieldnames = ['Timestamp', 'language', 'problem']

    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('favorites.csv', 'a') as file:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer = DictWriter(file, fieldnames=fieldnames)
        # prepare data
        new_data = {}
        # for i in len(fieldnames):
        for i in range(3):
            new_data[fieldnames[i]] = fields[i]
        # Pass the list as an argument into
        writer.writerow(new_data)

        print(f"Language: {language_value}, Problem: {problem_value}")

    print(f"Data Created Successfuly..")
