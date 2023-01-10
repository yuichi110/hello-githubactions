import requests


def get_hello():
    requests.get("https://www.google.com")
    return "hello"


if __name__ == "__main__":
    message = get_hello()
    print(message)
