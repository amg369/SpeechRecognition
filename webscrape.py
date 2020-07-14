# from io import BytesIO
import os
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from soupsieve.util import lower, upper

run = True


def StartSearch():
    try:
        search = input("Search for:")
        searched = lower((str(re.sub(" ", "", search))))
        dir_name = search.replace(" ", "_").lower()

        # Parse az-lyrics
        url = "https://www.azlyrics.com/lyrics/phoebebridgers/"
        url_edit = url + searched + ".html"
        r = requests.get(url_edit)

        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text()
        g_text = (text.split("Phoebe Bridgers Lyrics", 1)[1]).split("Submit Corrections", 1)[0]
        edit_text = (g_text.split('"' + search.title() + '"', 1)[1]).strip()

        f = open("./lyrics/" + search + ".txt", "w+")
        f.write(edit_text)
    except:
        print("That's not a Phoebe song")
        run = False


while run is True:
    StartSearch()
