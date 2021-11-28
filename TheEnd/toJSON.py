import json

from tovar import nounlist2
from price import nounlist1

def convertToJSON():
    with open("D:\Python\TheEnd\ tovar_json.json", "w") as write_file:
        json.dump(nounlist2, write_file)

def convertInJSON():
    with open("D:\Python\TheEnd\price_json.json", "w") as write_file:
        json.dump(nounlist1, write_file)