"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on
the New York Times homepage. https://www.nytimes.com/
"""


def print_html():
    from bs4 import BeautifulSoup
    import urllib.request

    with urllib.request.urlopen('http://pudim.com.br/') as response:
        soup = BeautifulSoup(response, 'html.parser')
        print(soup.prettify())


    """import requests
    from bs4 import BeautifulSoup

    base_url = 'http://www.pudim.com.br'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "lxml")

    for story_heading in soup.find_all(class_="container"):
        if story_heading.a:
            print(story_heading.a.text.replace("\n", " ").strip())
        else:
            print(story_heading.contents[0].strip())
    """

if __name__ == '__main__':
    print_html()
