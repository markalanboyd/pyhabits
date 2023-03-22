# pyenv activate pyhabits-3.11.2
# https://pixe.la/v1/users/markalanboyd/graphs/weightchange.html
import dotenv
import os
import requests
import datetime
from nicegui import ui

# Constants
dotenv.load_dotenv()
TOKEN = os.environ.get("TOKEN")
USER_NAME = os.environ.get("USER_NAME")
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_ENDPOINT_GRAPHS = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"


# Variables
create_user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_colors_dict = {
    "green": "shibafu",
    "red": "momiji",
    "blue": "sora",
    "yellow": "ichou",
    "purple": "ajisai",
    "black": "kuro",
}

graph_id = "weightchange" # ^[a-z][a-z0-9-]{1,16}
graph_name = "Daily Weight Change"
graph_unit = "lbs change"
graph_type = "float" # int or float
graph_color = graph_colors_dict["green"]


graph_parameters = {
    "id": graph_id,
    "name": graph_name,
    "unit": graph_unit,
    "type": graph_type,
    "color": graph_color,
}

pixel_url = f"{PIXELA_ENDPOINT_GRAPHS}/{graph_id}"
pixel_date = datetime.datetime.now().strftime("%Y%m%d")
pixel_quantity = "-2"
pixel_optionalData = ""

pixel_parameters = {
    "date": pixel_date,
    "quantity": pixel_quantity,
    "optionalData": pixel_optionalData,
}

# Functions
def pixela_create_user(parameters):
    response = requests.post(url=PIXELA_ENDPOINT,
                             json=parameters)
    response.raise_for_status()
    print(response.text)

def pixela_create_graph(parameters):
    response = requests.post(url=PIXELA_ENDPOINT_GRAPHS,
                             json=parameters,
                             headers=HEADERS)
    response.raise_for_status()
    print(response.text)

def pixela_post_pixel(parameters):
    response = requests.post(url=pixel_url,
                             json=parameters,
                             headers=HEADERS)
    response.raise_for_status()
    print(response.text)

# def ui_create_user() -> None:
    ui.checkbox("I agree to the terms and conditions")
    ui.checkbox("I am not a minor")
    ui.button('Register')

def main() -> None:
    # ui_create_user()
    # ui.run(title="pyhabits")
    # pixela_create_user(create_user_params)
    # pixela_create_graph(graph_parameters)
    pixela_post_pixel(pixel_parameters)
    pass


# Main
if __name__ in {"__main__", "__mp_main__"}:
    main()
    