import wikipedia
from bs4 import BeautifulSoup
from wikipedia import search, summary, page, DisambiguationError

search_input = input("Enter page title:")
while search_input != "":
    try:

        search(search_input)
        summary(search_input)
        page(search_input, auto_suggest= False)

    except NotFoundError:
        print(f"Page id {search_input} does not match any pages. Try another id!")
    except DisambiguationError:
        print(f"We need a more specific title. Try one of the following, or a new search")
        print(BeautifulSoup)
        page(search_input)
    search(search_input)
    summary(search_input)


