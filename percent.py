import numpy as np
import requests
import json

per = []
n = 0
res = requests.get("https://covid19-api.org/api/status")
items = res.json()
length = len(items)
while n < length:
    per.append(items[n]["cases"])
    n += 1
print(per)
print("90 перцентиль:", np.percentile(per, 90))