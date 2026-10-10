import requests


def build_request(url: str) -> requests.PreparedRequest:
    return requests.Request("GET", url, params={"q": "x"}).prepare()
