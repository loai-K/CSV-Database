from csv import DictReader


class Databse:
    language_counts = {}
    problem_counts = {}

    with open('favorites.csv', 'r') as file:
        reader = DictReader(file)
        # next(reader)
        for row in reader:
            # print(row['language'] + ' ' + row['problem'])
            language = row['language'].lower().strip()
            problem = row['problem'].lower().strip()

            if language not in language_counts:
                language_counts[language] = 0

            language_counts[language] += 1

            if problem not in problem_counts:
                problem_counts[problem] = 0

            problem_counts[problem] += 1


class main:
    data = Databse()
    print("Language Counts")
    for index in data.language_counts:
        print(f"{index}: {data.language_counts[index]}")

    print()
    print("Problem Counts")
    # for index in sorted(problem_counts, reverse=False):
    for index in sorted(data.problem_counts, key=lambda problem_key:Databse.problem_counts[problem_key], reverse=False):
        print(f"{index}: {data.problem_counts[index]}")