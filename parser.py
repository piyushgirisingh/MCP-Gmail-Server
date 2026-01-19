import base64
from bs4 import BeautifulSoup

def extract_text(payload):
    if "body" in payload and "data" in payload["body"]:
        return base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8")

    for part in payload.get("parts", []):
        if part["mimeType"] == "text/html":
            html = base64.urlsafe_b64decode(
                part["body"]["data"]
            ).decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            return soup.get_text()

    return ""
