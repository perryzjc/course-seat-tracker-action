import requests
from bs4 import BeautifulSoup
import json


headers = {
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
payload=base64.b64decode("eyJzZWN0aW9uSWQiOiIyNDczODUiLCJzdHVkZW50SWQiOm51bGx9")


def fetch_waitlist_seat():
    try:
        response = requests.request("POST", "https://selfservice.elcamino.edu/Student/Courses/SectionDetails", headers=headers, data=payload)
        # Parse the JSON response
        data = json.loads(response.text)

        # Extract the AvailabilityDisplay field and split to get the waitlist number
        availability_display = data.get("AvailabilityDisplay", "")
        waitlist_number = availability_display.split('/')[-1].strip()

        return waitlist_number
    
    except Exception as e:
        return f"Error: {e}"
    
# Fetch the waitlist seat
waitlist_seat = fetch_waitlist_seat()
print("Waitlist Number:", waitlist_seat)
