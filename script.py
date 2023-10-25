import requests
from bs4 import BeautifulSoup
import json
import sys

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    data_element = soup.find(attrs={'data-enrollment': True})
    if data_element:
        return data_element['data-enrollment']
    else:
        print("Could not find the required element on the page.")
        sys.exit(1)

def extract_data(data_json):
    try:
        data = json.loads(data_json)
        waitlisted = data.get('available', {}).get('enrollmentStatus', {}).get('waitlistedCount', 0)
        max_waitlist = data.get('available', {}).get('enrollmentStatus', {}).get('maxWaitlist', 0)
        return waitlisted, max_waitlist
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        sys.exit(1)

def main(url):
    html = get_html(url)
    data_json = parse_html(html)
    waitlisted, max_waitlist = extract_data(data_json)

    if should_exit_1(waitlisted, max_waitlist):
        print(f"Condition met for exit 1. {waitlisted} out of {max_waitlist} spots are taken.")
        sys.exit(1)
    else:
        print(f"Condition not met for exit 1. {waitlisted} out of {max_waitlist} spots are taken.")
        sys.exit(0)

def should_exit_1(waitlisted, max_waitlist):
    # Define the condition for exit 1 here
    return max_waitlist - waitlisted > 0

if __name__ == "__main__":
    url = "https://classes.berkeley.edu/content/2024-spring-compsci-168-001-lec-001"
    main(url)
