from flask import Flask, request
from bs4 import BeautifulSoup
import requests
import json
from flask_cors import CORS, cross_origin



app = Flask(__name__)
CORS(app, origins='http://localhost:3000')
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About page'

@app.route('/submit', methods=['POST'])
@cross_origin()
def submit():
    # decode bytes to string-
    data = request.data.decode('utf-8')
    print(data)

    def get_links(query):
        url_query = query
        links = []
        if " " in query:
            url_query = query.replace(" ", "+")
        url = "https://www.bing.com/search?q=" + url_query
        if get_tags(url, "a", "href") == False:
            links.append(False)
        else:
            hrefs = get_tags(url, "a", "href")
            for ref in hrefs:
                ref = str(ref)
                if "http" in ref and "youtube" not in ref:
                    links.append(ref)
                if len(links) == 10:
                    break
            return links


    def get_tags(url, tag, property):
        content = []
        try:
            site = requests.get(url)
        except:
            print("ERROR HANDLER WORKED")
        html = BeautifulSoup(site.text,"html.parser")
        targets = html.findAll(tag)

        for target in targets:
            content.append(target.get(property))
        return content


    def get_text(link):
        if link != False:
            text = []
            site = requests.get(link)
            html = BeautifulSoup(site.text,"html.parser")
            text_tags = ["h1", "h2", "h3", "p", "span", "li"]
            for tag in text_tags:
                targets = html.findAll(tag)
                for target in targets:
                    if target.text:
                        text.append(target.text)           
            return text


    def build_dict(links):
        print(links)
        keys = [i for i in range(len(links))]
        values = []
        for link in links:
            print("* \n")
            values.append(get_text(link))
        return {k:v for (k,v) in zip(keys, values)}
    
    scrape = build_dict(get_links(data))
    # What the POST request returns:
    return json.dumps(scrape)

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


