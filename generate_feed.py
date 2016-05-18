from lxml import etree
import config
import dateutil.parser
import email.utils
import time

def default(el, text):
    if text is None:
        el.text = "Untitled"
    else:
        el.text = text

def pubdate(el, date):
    d = dateutil.parser.parse(date)
    timestamp = time.mktime(d.timetuple())
    el.text = email.utils.formatdate(timestamp)

def enclosure(el, url):
    el.attrib["url"] = url
    el.attrib["type"] = "audio/mpeg"
    # should replace it by actual length, but this doesn't hurt much
    el.attrib["length"] = "100"

dispatch_dict = {
        "title": default,
        "link": default,
        "guid": default,
        "description": default,
        "enclosure": enclosure,
        "pubDate": pubdate,
        "category": default
}

class PodcastFeed:

    def __init__(self, attributes, entries):
        self.attributes = attributes
        self.entries = entries
        self.feed = etree.Element("rss", attrib={"version": "2.0"},
                                  nsmap=config.NSMAP)
        self.channel = etree.SubElement(self.feed, "channel")

    def process_attribute(self, root, attr, text):
        el = etree.SubElement(root, attr)
        if isinstance(text, dict):
            for k, v in text.items():
                self.process_attribute(el, k, v)
        elif attr == "{{{}}}category".format(config.NSMAP["itunes"]):
            el.attrib["text"] = text
        else:
            el.text = text

    def generate_feed(self):
        for attr, text in self.attributes.items():
            self.process_attribute(self.channel, attr, text)
        for i in self.entries:
            self.process_item(i)

    def write_to_file(self, filename):
        with open(filename, "wb") as f:
            tree_str = etree.tostring(self.feed, pretty_print=True)
            f.write(tree_str)

    def process_item(self, item):
        item_el = etree.SubElement(self.channel, "item")
        for attr, func in dispatch_dict.items():
            el = etree.SubElement(item_el, attr)
            dispatch_dict[attr](el, item[attr])


    def add_from_rss(self, rss_file):
        channel = etree.parse(rss_file).getroot().find("channel")
        items = channel.findall("items")
