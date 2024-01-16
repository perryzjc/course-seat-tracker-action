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
        data_element = soup.find(attrs={'data-enrollment': True})
        if data_element:
            return self.extract_data(data_element['data-enrollment'])
        else:
            print("Could not find the required element on the page.")
            sys.exit(1)

    def extract_data(self, data_json):
        try:
            data = json.loads(data_json)
            # enrolled = data.get('available', {}).get('enrollmentStatus', {}).get('enrolledCount', 0)
            total_open_seats = self.calculate_total_open_seats(data.get('available', {}))
            available = total_open_seats > 0
            message = f"CS160 Discussion has {total_open_seats} seats opened!"
            return available, message
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            sys.exit(1)

    @staticmethod
    def calculate_total_open_seats(available):
        """Algorithm to calculate total open seats for UC Berkeley's courses

        Note: it's not a simply max_enroll - enrolled_count
        Below code refers to:
        https://classes.berkeley.edu/sites/default/files/js/js_wkZa4u4BCnSi4JXgkE3Om2OjgDKSaG35ZwAKoHBOzqI.js

        >>> available = {
        ...        'combination': {
        ...            'maxEnrollCombinedSections': 90,
        ...            'enrolledCountCombinedSections': 118
        ...        },
        ...        'enrollmentStatus': {
        ...            'maxEnroll': 74,
        ...            'enrolledCount': 72
        ...        }}
        >>> CS160.calculate_total_open_seats(available)
        0
        """
        if 'combination' in available:
            combined_open_seats = available['combination']['maxEnrollCombinedSections'] - available['combination']['enrolledCountCombinedSections']
            per_class_open_seats = available['enrollmentStatus']['maxEnroll'] - available['enrollmentStatus']['enrolledCount']
            value = min(combined_open_seats, per_class_open_seats)
            return max(value, 0)
        else:
            return max(available['enrollmentStatus']['maxEnroll'] - available['enrollmentStatus']['enrolledCount'], 0)
