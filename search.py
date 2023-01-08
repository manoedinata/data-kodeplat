import json
import sys

with open("kode_plat.json", "r") as f:
    data = json.load(f)

searched = next((item for item in data if item["kode"] == sys.argv[1]), None)
if searched:
    print(f"{sys.argv[1]}: {searched['daerah']}")
