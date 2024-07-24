from bs4 import BeautifulSoup
import json
import sys
from courses.base_course import BaseCourse

class BIOENG_100(BaseCourse):
    def __init__(self):
        super().__init__("https://classes.berkeley.edu/content/2024-fall-bioeng-100-001-lec-001")

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        data_element = soup.find(attrs={'data-enrollment': True})
        if data_element:
            return self.extract_data(data_element['data-enrollment'])
        else:
            print("Could not find the required element on the page.")
            sys.exit(1)

    def extract_data(self, data_json):
        try:
            data = json.loads(data_json)
            waitlisted = data.get('available', {}).get('enrollmentStatus', {}).get('waitlistedCount', 0)
            available = waitlisted < 50
            message = f"{waitlisted} waitlisted out of 50 spots"
            return available, message
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            sys.exit(1)
