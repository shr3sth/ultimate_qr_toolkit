import json
from urllib.parse import urlparse


BLOCKLIST_FILE = "data/blocked_domains.json"


def check_url_safety(url):
    try:
        domain = urlparse(url).netloc.lower()

        with open(BLOCKLIST_FILE, "r") as file:
            blocked_domains = json.load(file)

        if domain in blocked_domains:
            return False

        return True

    except Exception:
        return True
