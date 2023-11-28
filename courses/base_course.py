import requests
import sys

class BaseCourse:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            sys.exit(1)

    def parse_html(self, html):
        raise NotImplementedError("parse_html method must be implemented by the subclass")

    def check_availability(self):
        html = self.get_html()
        print(f"HTML: {html}")
        available, message = self.parse_html(html)
        if available:
            print(f"{self.__class__.__name__} is available! {message}")
            return f"{self.__class__.__name__} is available! {message}"
        else:
            print(f"{self.__class__.__name__} is not available. {message}")
            return None
