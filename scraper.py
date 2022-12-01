import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    html_elements = soup.findAll("a", {"title": "Wikipedia:Citation needed"})
    return len(html_elements)


def get_citations_needed_report(url):
    text = ""
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    html_elements = soup.findAll("a", {"title": "Wikipedia:Citation needed"})
    for html_element in html_elements:
        text += html_element.parent.parent.parent.text
        text += "\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n"
    return text


if __name__ == '__main__':
    URL = "https://en.wikipedia.org/wiki/Interpreter_(computing)"
    print(f"The number of citations needed are {get_citations_needed_count(URL)}")
    print("The passages that need citations are:")
    print("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")
    print(get_citations_needed_report(URL))
