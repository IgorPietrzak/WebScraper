from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.bing.com/search?q=translation'


def get_tags(url, tag, property):
        content = []
        driver.get(url)
        tags = driver.find_elements_by_tag_name(tag)
        for tag in tags:
              attr = tag.get_attribute(property)
              content.append(attr)
        return content


def get_links(q):
    links = []
    if " " in q:
        url_query = q.replace(" ", "+")
    url = "https://www.bing.com/search?q=" + url_query
    a_tags = get_tags(url,"a", "href")
    for a in a_tags:
          if "http" in str(a):
                links.append(a)
    return links


print(get_links("Translation services"))


driver.quit()
