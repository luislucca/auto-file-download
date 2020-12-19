# Code made by Luís Fernando de Lucca Costa Souza
# The objective is to automate a file download from Danish Financial Supervisory Authority

# PIP packages:
# pip install requests2

import time
from datetime import date
import requests

def download_file(url, file_name = ''):
    # Making the url request
    req = requests.get(url)

    try:
        # Defines the file name as the given parameter
        if file_name:
            pass
        # Or, defines the file name as below
        else:
            # Defining the file name with the download date
            down_date = date.today().strftime("%d-%m-%y")
            title = req.url[url.rfind('/')+1:url.rfind('-')]
            type = req.url[url.rfind('.'):]
            file_name = f"{title}_{down_date}{type}"

        # Creating a new file with the data retrieved from the request
        with open(file_name, "wb") as f:
            for chunk in req.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return file_name

    except Exception as e:
        print(e)
        return None

# Setting the URL
url = "https://www.finanstilsynet.dk/-/media/Tal-og-fakta/PEP/PEP_listen-xlsx.xlsx"

# Calling the function
download_file(url)