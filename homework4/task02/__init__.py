import requests


def count_dots_on_i(url):
    try:
        response = requests.get(url)
        return response.text.count("i")
    except requests.exceptions.RequestException as err:
        raise ValueError("Unreachable URL") from err
