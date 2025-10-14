# dictionaries
# country: capital, pop, %
country_to_data = {}
with open("countries.csv", "r") as in_file:
    for line in in_file:
        # continue
max_length_country = max((len(country) for country in country_to_data))
max_length_capital = max((len(capital) for capital in country_to_data))
max_length_population = max((len(str(population)) for population in country_to_data))
max_length_percentage = max((len(percentage) for percentage in country_to_data))
for country, capital, population, percentage in sorted(country_to_data.items()):
#     print(f"{name:<{max_length_name}} = {score:>{max_length_score}}")
print(f"{country:<{max_length_country}} - {capital: <{max_length_capital}} {population:<{max_length_population}} ({percentage:<{max_length_percentage_of_country}})")
# new line