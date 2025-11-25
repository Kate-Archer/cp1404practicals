"""
Wikipedia prac 10
"""

import wikipedia
from wikipedia import DisambiguationError, PageError

search_input = input("Enter page title: ")
while search_input != "":
    try:
        # Try to load the page normally
        print(wikipedia.search(search_input))
        print(wikipedia.summary(search_input))
        print(wikipedia.page(search_input, auto_suggest=False).url)

    except PageError:
        print(f"Page id '{search_input}' does not match any pages. Try another id!")

    except DisambiguationError as error:
        print("We need a more specific title. Try one of the following:")
        print(error.options)  # Show list of options

    search_input = input("\nEnter page title: ")

print("Thank you.")
