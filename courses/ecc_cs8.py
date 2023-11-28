import requests
import json
import sys
import base64
from courses.base_course import BaseCourse

class ECC_CS8(BaseCourse):
    def __init__(self):
        super().__init__("https://selfservice.elcamino.edu/Student/Courses/SectionDetails")
        self.headers = {
          'content-length':'39',
          'sec-ch-ua':'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
          'sec-ch-ua-mobile':'?0',
          '__isguestuser':'true',
          'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
          'content-type':'application/json, charset=UTF-8',
          'accept':'application/json, text/javascript, */*; q=0.01',
          'x-requested-with':'XMLHttpRequest',
          '__requestverificationtoken':'1X7gOIlyNSWCXEGBE5mlzIi9VMAyRYJ4PmUy-RfMxDkSry4uMFP7PYtUCyHcd7Z6jP9AULMMuIOALeWdjziddGeENtzB1zVXdbAToX3E2jc1',
          'origin':'https://selfservice.elcamino.edu',
          'sec-fetch-site':'same-origin',
          'sec-fetch-mode':'cors',
          'sec-fetch-dest':'empty',
          'referer':'https://selfservice.elcamino.edu/Student/Courses/Search?keyword=CSCI-8',
          'cookie':'__RequestVerificationToken_L1N0dWRlbnQ1=eu4xFpxLZkqreQcsa9aD8A1YPNOXhI9VoiJPW504BJI9NsL321zT5wOG-AgZJr5xXNBx4fZzx4bWTxsZ7QEryvZNuElfgWF8APmmU_AGTyA1'
        }
        self.payload = base64.b64decode("eyJzZWN0aW9uSWQiOiIyNDczODUiLCJzdHVkZW50SWQiOm51bGx9")

    def get_html(self):
        try:
            response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error while fetching data: {e}")
            # sys.exit(1)

    def parse_html(self, data_json):
        try:
            data = json.loads(data_json)
            availability_display = data.get("AvailabilityDisplay", "")
            waitlist_number = availability_display.split('/')[-1].strip()
            max_waitlist = 10
            available = max_waitlist - int(waitlist_number) > 0
            message = f"{waitlist_number} out of {max_waitlist} spots are waitlisted."
            return available, message
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            # sys.exit(1)
