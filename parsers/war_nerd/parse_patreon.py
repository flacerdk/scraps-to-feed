import json
import codecs
import urllib.request

def parse_json(url):
    reader = codecs.getreader("utf-8")
    json_feed = json.load(reader(urllib.request.urlopen(url)))
    items = []

    for post in json_feed["data"]:
        item = {}
        data = post["attributes"]
        guid = data["post_file"]["url"]
        item["title"] = data["title"]
        item["link"] = data["url"]
        item["guid"] = guid
        item["description"] = data["content"]
        item["enclosure"] = guid.replace("https://", "http://")
        item["pubDate"] = data["created_at"]
        item["category"] = "Podcasts"
        items.append(item)

    return items
