'''Self-made BigBlueButton (video conference website) scraper'''

import requests
import webbrowser

def getconference(url):
    """Get data about a conference."""

    try:
        data = requests.get(url).text
    except:
        return False

    conference = {}
    conference["id"] = url.split("://")[1].split("/")[2]
    conference["host"] = url.split("://")[1].split("/")[0].replace('" ', "")
    conference["host_id"] = url.split("://")[1].split("/")[2].split("-")[0]
    conference["room"] = " ".join(data.split("<title>")[1].split("</title>")[0].split()[1:])
    conference["owner"] = " ".join(data.split(")</h5>")[0].split("block\">")[1].split()[:-1])
    conference["random_token"] = data.split("<meta name=\"csrf-token\" content=\"")[1].split("\" />")[0]

    return conference

def getsession(url):
    """Get information about a session."""
    session = {}
    session["token"] = url.split("sessionToken=")[1].split("&")[0]
    session["server"] = url.split("//bbb")[1].split(".")[0]
    session["valid_base_url"] = "200" in str(requests.get(url)) 
    return session

def getslides(url):
    """Returns valid URLs for all avaiable presentation slides."""
    urls = []
    url_prefix = url.split("/svg/")[0]
    for slide in range(1, 100):
        url = url_prefix + "/svg/" + str(slide)
        if "200" in str(requests.get(url)):
            urls.append(url)
        else:
            return urls
  
if __name__ == "__main__":
    print(getslides("https://bbb.talpaworld.de/bigbluebutton/presentation/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-0000000000000/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-0000000000000/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-0000000000000/svg/000"))
    print()
    print(getsession("https://bbb14.bbb-meeting.de/html5client/join?sessionToken=XXXXXXXXXXXXXXXX"))
    print()
    print(getconference("https://bbb-meeting.de/b/XXX-XXX-XXX-XXX"))
