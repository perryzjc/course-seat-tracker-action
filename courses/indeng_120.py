from bs4 import BeautifulSoup
import json
import sys
from courses.base_course import BaseCourse

class INDENG_120(BaseCourse):
    def __init__(self):
        super().__init__("https://classes.berkeley.edu/content/2024-spring-indeng-120-1-lec-1")

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
            max_waitlist = data.get('available', {}).get('enrollmentStatus', {}).get('maxWaitlist', 0)
            available = max_waitlist - waitlisted > 0
            message = f"{waitlisted} out of {max_waitlist} spots are taken."
            return available, message
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            sys.exit(1)
