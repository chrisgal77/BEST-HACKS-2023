# Made by Jakub Olszewski 2023
# Best Hacks 2023

import requests
import re
import tqdm
import codecs
from bs4 import BeautifulSoup

BASE_LINK = "https://visitwroclaw.eu/"

REGEX_OUTER = r"\<li\ class\=\"col\-sm\-6\ col\-md\-3\"\>\s\<a\ href=\"miejsce\/([\w-]+)\"\ class\=\"lnkBlock\""
PAGE_NUMBER = r"\<a\ href\=\"miejsca\/kultura\/strona\,(\d+)"

REGEX_TITLE = r"\<h1\ class\=\"txtMainTitle\"\>\s+([\w\s]+)\s\<\/h1\>"
# REGEX_DESCRIPTION = (
#     r"\<h2\ dir\=\"ltr\"\ id\=\"header2\">Co\ można\ zobaczyć\ w\ .+\s([\s\S]+)\<div\>"
# )
REGEX_DESCRIPTION = (
    r"\<h2\ dir\=\"ltr\"\>Co\ można\ zobaczyć\ w(.+)\<\/li\>\\n\<\/ul\>\\n\<h2\ dir\=\"ltr\"\>"
)
REGEX_ADDRESS = r"\<div\ class\=\"boxContactData\"\>\s\<p\ class\=\"txtBold\"\>([\w\s\.\,]+)\<br\>([\d\-\s\w]+)\<\/p\>"

r = requests.get(BASE_LINK + "miejsca/kultura/")
page_max = max([int(i) for i in re.findall(PAGE_NUMBER, r.text)])


def get_link(page: int) -> str:
    if page == 0:
        return ""
    return f"strona,{page}/"


def get_pannel_links(page_max: int) -> list[str]:
    links: list[str] = []
    for i in range(page_max):
        links.extend(
            re.findall(REGEX_OUTER, requests.get(BASE_LINK + "miejsca/kultura/" + get_link(i)).text)
        )
    return links


def get_place_data(place_link: str) -> dict[str | None, str | None, str | None]:
    r = requests.get(BASE_LINK + "miejsce/" + place_link)
    soup = BeautifulSoup(r.text, "html.parser")

    name = re.findall(REGEX_TITLE, r.text)
    desc = soup.find("div", string="Co można zobaczyć w")
    addr = re.findall(REGEX_ADDRESS, r.text)

    name = name[0] if len(name) else None
    addr = "".join(addr[0]) if len(addr) else None

    return (name, desc, addr)


if __name__ == "__main__":
    with codecs.open("data.csv", "w", "utf-8") as file:
        file.write("Place; Description; Address; full_success\n")
        links = get_pannel_links(page_max)
        for link in tqdm.tqdm(links):
            (name, desc, addr) = get_place_data(link)
            file.write(f"{name};{desc};{addr};{int(None not in [name, desc, addr])}\n")
            break
