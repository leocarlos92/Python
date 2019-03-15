"""
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.
"""


def print_html_file():
    from bs4 import BeautifulSoup
    with open('/home/leonarbc/PycharmProjects/training/practicepython/html_doc.html', 'r+') as html_doc:
        soup = BeautifulSoup(html_doc, "html.parser")
        print(soup.prettify())
        print(soup.title)
        print(soup.title.name)
        print(soup.title.string)
        print(soup.title.parent.name)
        print(soup.p)
        print(soup.p['class'])
        print(soup.a)
        print(soup.find_all('a'))
        print(soup.find(id='link2'))


def write_text_from_html_web_site_into_file():
    from bs4 import BeautifulSoup
    import requests
    base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")
    with open("/home/leonarbc/PycharmProjects/training/practicepython/Exercise_19_text_from_webiste.txt", 'w') as file:
        for paragraph in soup.body.find_all('p'):
            file.write(paragraph.text + '\n')


if __name__ == '__main__':
    write_text_from_html_web_site_into_file()
