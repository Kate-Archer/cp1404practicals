"""
CP1404 Practical
Wimbledon data-reading, processing and displaying
Estimate: 30
Time: 1:56 - 2:20
"""


FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read data file and print details about Wimbledon champions and countries"""
    records = load_records(FILENAME)
    champion_to_score, countries = process_records(records)
    display_results(champion_to_score, countries)


def process_records(records):
    """Create dictionary of champions and set of countries from records (list of lists)"""
    champion_to_score = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_score[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_score[record[INDEX_CHAMPION]] = 1
        return champion_to_score, countries


def display_results(champion_to_score, countries):
    """Display champion to countries neatly"""
    print("Wimbledon Champions: ")
    for name, score in champion_to_score.items():
        max_length_score = max(len(str(score)) for score in champion_to_score.values())
        max_length_name = max(len(str(name)) for name in champion_to_score.keys())
        print(f"{name:<{max_length_name}} : {score:<{max_length_score}}")
        # print(name, score)
        print(f"\nThese {len(countries)} have won Wimbledon:")
        print(",".join(sorted(countries)))


def load_records(filename):
    """Load records from wimbledon file in list of lists form"""
    records = []
    # Skip first line as this contains the headers
     with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
