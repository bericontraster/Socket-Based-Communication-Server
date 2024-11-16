# Importing libs
import random
import requests

def zisquote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        quote = data['q']
        author = data['a']
        return f"{quote} - {author}"
    else:
        return "Aliens don't motivate."


# Generating random response


# Ai Chat Bot
def airesponse(message):
    
    # Brain
    if "how" in message:
        return "I'm good how are you human?"
    elif message in ['create', 'made', 'created']:
        return "I was made by Aliens. I moved to earth recently."
    elif message in ['What is qoute of the day?', 'qoute', 'motivate me']:
        return zisquote()
    else:
        return "Not included in if/else ;)"

def poweron(message):
    return airesponse(message)


