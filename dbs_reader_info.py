import csv

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

with open("drug_bank_info_for_list.txt", "r") as file: 
    lines = file.read().split("\n")

    new_lines = []

    for line in lines:
        if "<strong>" in line:
            new_lines.append(line)
        else:
            new_lines.append("<p>No info</p>")

    f = open("drug_bank_info.txt", "w")
    for line in new_lines:
        f.write(str(line))
        f.write("\n")
    f.close()
