"""
CP1404 Practical
Wimbledon data-reading, processing and displaying
Estimate: 30
Time: 1:56
"""

def main():
    # read file:
    CHAMPION_TO_SCORE = {}
    # year, country, champion, country, runner-up, score in final
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.split(",")
            champion = parts[2]
            champion = set()
            print(champion)
    max_length_score = max(len(score) for  score in CHAMPION_TO_SCORE(score)
    max_length_champion = max(len(champion) for champion in CHAMPION_TO_SCORE(champion))
    print(f"{champion:<{max_length_champion}} : {score:<{max_length_score}}")

    countries = parts[1]
    print(f"These {number_of_countries} have won Wimbledon:n\ {countries.join()}")









main()


















#
# FILENAME = "wimbledon.csv"
# INDEX_COUNTRY = 1
# INDEX_CHAMPION = 2
#
#
# def main():
#     """Read data file and print details about Wimbledon champions and countries."""
#     records = load_records(FILENAME)
#     champion_to_count, countries = process_records(records)
#     display_results(champion_to_count, countries)
#
#
# def process_records(records):
#     """Create dictionary of champions and set of countries from records (list of lists)."""
#     champion_to_count = {}
#     countries = set()
#     for record in records:
#         countries.add(record[INDEX_COUNTRY])
#         try:
#             champion_to_count[record[INDEX_CHAMPION]] += 1
#         except KeyError:
#             champion_to_count[record[INDEX_CHAMPION]] = 1
#     return champion_to_count, countries
#
#
# def display_results(champion_to_count, countries):
#     """Display champions and countries"""
#     print("Wimbledon Champions: ")
#     for name, count in champion_to_count.items():
#         print(name, count)
#     print(f"\nThese {len(countries)} countries have won Wimbledon: ")
#     print(", ".join(sorted(countries)))
#
#
# def load_records(filename):
#     """Load records from file in list of lists form."""
#     records = []
#     with open(filename, "r", encoding="utf-8-sig") as in_file:
#         in_file.readline()  # Remove CSV header row
#         for line in in_file:
#             parts = line.strip().split(",")
#             records.append(parts)
#     return records
#
#
# main()
