FEED_FILE = "war_nerd.rss"
SOURCE_URI = "posts.json"

ATOM = "http://www.w3.org/2005/Atom"
ITUNES = "http://www.itunes.com/dtds/podcast-1.0.dtd"

NSMAP = {
        "atom": ATOM,
        "itunes": ITUNES
}

FEED_ATTRIBUTES = {
    "title": "Radio War Nerd",
    "description": "Radio War Nerd",
    "link": SOURCE_URI,
    "language": "en-us",
    "{%s}subtitle" % (ITUNES): "Radio War Nerd",
    "{%s}author" % (ITUNES): "Mark Ames and Gary Brecher",
    "{%s}summary" % (ITUNES): "Radio War Nerd",
    "{%s}explicit" % (ITUNES): "Yes",
    "{%s}owner" % (ITUNES): {
        "{%s}name" % (ITUNES): "Me",
        "{%s}email" % (ITUNES): "me@example.com"
    },
    "{%s}category" % (ITUNES): "History",
}
