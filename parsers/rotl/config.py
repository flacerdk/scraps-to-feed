FEED_FILE = "rotl.rss"
SOURCE_URI = "rotl.json"

ATOM = "http://www.w3.org/2005/Atom"
ITUNES = "http://www.itunes.com/dtds/podcast-1.0.dtd"

NSMAP = {
        "atom": ATOM,
        "itunes": ITUNES
}

FEED_ATTRIBUTES = {
    "title": "Roderick on the Line",
    "description": "Roderick on the Line",
    "link": SOURCE_URI,
    "language": "en-us",
    "{%s}subtitle" % (ITUNES): "Roderick on the Line",
    "{%s}author" % (ITUNES): "Merlin Mann and John Roderick",
    "{%s}summary" % (ITUNES): "Roderick on the Line",
    "{%s}explicit" % (ITUNES): "Yes",
    "{%s}owner" % (ITUNES): {
        "{%s}name" % (ITUNES): "Me",
        "{%s}email" % (ITUNES): "me@example.com"
    },
    "{%s}category" % (ITUNES): "Comedy",
}
