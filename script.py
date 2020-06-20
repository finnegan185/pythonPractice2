import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet(input("Who are you? ")))

r = requests.get('https://coreyms.coZam')
print(r.status_code)
