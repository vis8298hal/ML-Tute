import urllib.request
import json
import pandas as pd
from html.parser import HTMLParser
from xml.dom import minidom
df_dict = {}
paragraphs = 0
def print_json_data(json_data):
    if "title" in json_data["metadata"]:
        print(json_data["metadata"]["title"])
    print(json_data["metadata"]["count"])
    
    for i in json_data["features"]:
        properties = i["properties"]["place"]
        print(properties)
    print("--------------------------------------------------")
        
def get_normal_earthquakes(json_data):
    """ Any Earthquake having Msagnitude greater than 4.0 is considered as normal earthquake """
    for i in json_data["features"]:
        if i["properties"]["mag"] > 4.0:
            print(i["properties"]["place"],i["properties"]["mag"])
    print("--------------------------------------------------")

def get_felt_data(json_data):
    """Any Earthquake where atleast 1 Felt event is reported"""
    for i in json_data["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print(i["properties"]["place"], feltReports)

    print("--------------------------------------------------")

def get_url_data(url):
    weburl = urllib.request.urlopen(url)
    print(weburl.getcode())
    data = weburl.read()
    print(data)
    return data

def read_json_data(url):
    weburl = urllib.request.urlopen(url)
    if weburl.getcode() == 200:
        data = weburl.read()
        json_data = json.loads(data)
        print_json_data(json_data)
        get_normal_earthquakes(json_data)
        get_felt_data(json_data)

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        pos = self.getpos()
        print("At Line : ", pos[0], pos[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Data at : ",self.getpos()[0])

    def handle_starttag(self, tag, attrs):
        print("Start tag : ", tag)
        print("at Line : ", self.getpos()[0])

        global paragraphs
        if tag == "p":
            for attr in attrs:
                paragraphs += 1
        print("paragraph count is ", paragraphs)
        if len(attrs) > 0:
            for attr in attrs:
                print("Attributes : ", attr[0], "=", attr[1])
def read_html_data():
    parser = MyHTMLParser()
    f = open(r"C:\Users\kumar\Downloads\ML-Projects\Tutedude\Python-Adv\samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)

def read_xml_data():
    doc = minidom.parse(r"C:\Users\kumar\Downloads\ML-Projects\Tutedude\Python-Adv\samplexml.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    print("-----------------------------")
    skills = doc.getElementsByTagName("skill")
    for skill in skills:
        print(skill.getAttribute("name"), skill.getAttribute("value"))

    print("-----------------------------")
    print("Create new Skill Tag and assign to document")
    newskill = doc.createElement("skill")
    newskill.setAttribute("name", "SQL")
    doc.firstChild.appendChild(newskill)
    skills = doc.getElementsByTagName("skill")
    for skill in skills:
        print(skill.getAttribute("name"), skill.getAttribute("value"))

def main():
   #google_data = get_url_data("https://www.google.com")
    #read_json_data("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
    #read_html_data()
    read_xml_data()
    return 0

if __name__ == "__main__":
    main()