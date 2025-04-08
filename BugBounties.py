import requests

url= "https://xss-game.appspot.com/level1"

xss_payLoad = "<script>alert('XSS'),/script>"
response= requests.get(url + xss_payLoad)
if xss_payLoad in response.text:
    print("Potential XSS vulnerability detected!")
else:
    print("No XSS vulnerability detected.")