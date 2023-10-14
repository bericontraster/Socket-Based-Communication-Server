# Importing Libraries
from sources.countfetch import fetch
from sources.zischat import poweon

def response(message):
    # Input handling    
    message = str(message)
    message = message.lower()
    
    # Forwardning requests.
    if 'fetch' in message:
        details = fetch(message)
        return details
    else:
        return poweon(message)



