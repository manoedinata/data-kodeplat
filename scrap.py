import requests
from bs4 import BeautifulSoup
import json

URL = "https://ilmupengetahuanumum.com/kode-plat-nomor-tanda-nomor-kendaraan-bermotor-di-indonesia/"

req = requests.get(URL)
parse = BeautifulSoup(req.text, "html.parser")

table = parse.find_all("table")[1]
data = []
for col in table.find_all("tr")[1:]:
    kode = col.select_one("td:nth-of-type(1)").text
    daerah = col.select_one("td:nth-of-type(2)").text

    if col.select_one("td:nth-of-type(3)").findChildren("li"):
        cakupan = [x.text for x in col.select_one("td:nth-of-type(3)").findChildren("li")]
    else:
        if col.select_one("td:nth-of-type(3)").text.startswith("-") and len(col.select_one("td:nth-of-type(3)").text.split("-")) > 1:
            cakupan = col.select_one("td:nth-of-type(3)").text.split("-")[1:]
        else:
            cakupan = col.select_one("td:nth-of-type(3)").text

    data.append({
        "kode": kode,
        "daerah": daerah,
        "cakupan": cakupan,
    })

with open("kode_plat.json", "w") as f:
    json.dump(data, f, indent=4)

# print(json.dumps(data, indent=4))
