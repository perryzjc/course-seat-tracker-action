from bs4 import BeautifulSoup
import json
import sys
from courses.base_course import BaseCourse

class CS160(BaseCourse):
    """
    Different than other implementations, this class aims to find total open seats for the
    discussion section of CS160. Aims to find total open seat > 0;
    """
    def __init__(self):
        super().__init__("https://classes.berkeley.edu/content/2024-spring-compsci-160-999-dis-999")

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        data_element = soup.find(class_="fspmedium")
        if data_element:
            return self.extract_data(data_element)
        else:
            print("Could not find the required element on the page.")
            sys.exit(1)

    def extract_data(self, data):
        try:
            data = data.text
            disc_open_seats = int(data.strip())
            available = disc_open_seats > 0
            message = f"CS 160 discussion has {disc_open_seats} open seat now!"
            return available, message
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            sys.exit(1)
