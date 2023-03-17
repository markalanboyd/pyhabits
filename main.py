# pyenv activate pyhabits-3.11.2
import dotenv
import os
import requests
from nicegui import ui

# Constants
dotenv.load_dotenv()
TOKEN = os.environ.get("TOKEN")
USER_NAME = os.environ.get("USER_NAME")
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_ENDPOINT_CREATE_GRAPH = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"


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

# Functions
def pixela_create_user(parameters):
    response = requests.post(url=PIXELA_ENDPOINT,
                             json=parameters)
    print(response.text)

def pixela_create_graph(parameters):
    response = requests.post(url=PIXELA_ENDPOINT_CREATE_GRAPH,
                             json=parameters,
                             headers=HEADERS)
    print(response.text)

def ui_create_user() -> None:
    ui.checkbox("I agree to the terms and conditions")
    ui.checkbox("I am not a minor")
    ui.button('Register')

def main() -> None:
    # ui_create_user()
    # ui.run(title="pyhabits")
    # pixela_create_user(create_user_params)
    # pixela_create_graph(graph_parameters)
    pass


# Main
if __name__ in {"__main__", "__mp_main__"}:
    main()
    