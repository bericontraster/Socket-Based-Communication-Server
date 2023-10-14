# Importing Libraries
from sources.countfetch import fetch

def response(message):
    message = str(message)
    message = message.lower()
    print(message)
    if 'leri' in message:
        return "I knew it :). What can I do for you boss?"
    elif 'fetch' in message:
        details = fetch(message)
        return details
    else:
        return "SERVER RESPONDING!!!"

# userinput = input("# ")
# reponse = response(userinput)
# print(reponse)


