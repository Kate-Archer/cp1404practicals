import wikipedia
from wikipedia import search, summary, page



search_input = input("Please enter a page title or search phrase:")
while search_input != "":
    search(search_input)
    summary(search_input)
    page(search_input)
