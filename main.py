import requests
from datetime import datetime

USERNAME = "Your Username"
TOKEN = "your Token"
GRAPH_ID = "graph1"

# ------------------------Creating Account---------------------------#
pixela_endpoint = "https://pixe.la/v1/users"
user_config = {
    "token": TOKEN,  # like a password
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# connect to the api endpoint and send over the data of our account
"""response = requests.post(url=pixela_endpoint, json=user_config)
print(response.text)  # looking at the response sent from server"""
# DONE
# -------------------------------------------------------------------#

# -------------------------Creating Graph----------------------------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Python Coding Persistent",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

headers_token = {  # send the password in a secure way
    "X-USER-TOKEN": TOKEN
}

"""graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers_token)
print(graph_response.text)"""
# DONE
# -------------------------------------------------------------------#

# -------------------------Pixel Creation----------------------------#
today = datetime.today()  # get the date
today_str = today.strftime("%Y%m%d")  # turn it to string of this format: yyyymmdd

create_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
create_config = {
    "date": today_str,
    "quantity": "1"
}
"""create_response = requests.post(url=create_endpoint, json=create_config, headers=headers_token)
print(create_response.text)"""
# -------------------------------------------------------------------#

# --------------------------Pixel Update-----------------------------#
update_endpoint = f"{create_endpoint}/{today_str}"
update_config = {
    "quantity": "1"
}
update_response = requests.put(url=update_endpoint, json=update_config, headers=headers_token)
print(update_response.text)
# -------------------------------------------------------------------#

# --------------------------Pixel Delete-----------------------------#
delete_endpoint = update_endpoint  # delete a pixel from today's date
"""delete_response = requests.delete(url=delete_endpoint, headers=headers_token)
print(delete_response.text)"""
# -------------------------------------------------------------------#
