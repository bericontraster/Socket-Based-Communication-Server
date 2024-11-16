# Importing libraries
from countryinfo import CountryInfo

# Creaint a list of information.
countryDetails = []

# Input handling from client.
def inputHandling(clientMessage):
    clientMessage = str(clientMessage)
    return clientMessage.split('-', 1)[-1].strip()


# Tranfering the input for fetching details.
def getInfo(countryname):
    try:
        # Fetching json data form API.
        countryInformation = CountryInfo(countryname)
        
        # Region
        cRegion = countryInformation.region()
        cRegion = str(cRegion)
        countryDetails.append(cRegion)
        
        # Population
        cPop = countryInformation.population()
        cPop = str(cPop)
        countryDetails.append(cPop)
        
        # Currencies
        cCurr = countryInformation.currencies()
        cCurr = str(cCurr)
        countryDetails.append(cCurr)
        
        # Capital of country
        cCap = countryInformation.capital()
        cCap = str(cCap)
        countryDetails.append(cCap)
        
        # Timezone
        cTime = countryInformation.timezones()
        cTime = str(cTime)
        countryDetails.append(cTime)
        
        # Wiki
        cWiki = countryInformation.wiki()
        cWiki = str(cWiki)
        countryDetails.append(cWiki)

        details = cRegion + "=" +  cPop + "=" + cCurr + "=" + cCap + "=" + cTime + "=" + cWiki
        return details
    except:
        return "Invalid syntax or country name."


def fetch(clientMessage):
    countryName = inputHandling(clientMessage)
    details = getInfo(countryName)

    if details == "Invalid syntax or country name.":
        return "Invalid Syntax - fetch-countryname"
    else:
        return details
