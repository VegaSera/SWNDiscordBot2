### Uses the Behind the Name API to generate believable names

"""

-----------
YOU NEED A BEHIND THE NAME API KEY IN ORDER TO USE THIS
PUT IT IN THE .env FILE as BTN_KEY
If you do not you will get back an error instead of a random name
-----------

"""
from dotenv import load_dotenv
import os
import requests
import xml.etree.ElementTree as ET



load_dotenv()


def random_name(gender=None, usage="eng", randomsurname='yes', number=1, key=os.getenv("BTN_KEY")):
    if key == None:
        return 'Behind the name API key not set'
    if gender:
        url = f"https://www.behindthename.com/api/random.xml?usage={usage}&gender={gender}&randomsurname={randomsurname}&number={number}&key={key}"
    else:
        url = f"https://www.behindthename.com/api/random.xml?usage={usage}&randomsurname={randomsurname}&number={number}&key={key}"

    response = requests.get(url)
    root = ET.fromstring(response.content)

    return (root[0][0].text + ' ' + root[0][1].text)

if __name__ == '__main__':
    print(random_name())
