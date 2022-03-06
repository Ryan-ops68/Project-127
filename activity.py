import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver")
browser.get(start_url)
time.sleep(10)
def scrape():
    headers = ["name", "distance", "mass", "radius"]
    star_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    star_table = soup.find("table")
    temp_list = []
    table_rows = star_table.find_all("tr")
    for tr in table_rows:
        td = tr.find_all("td")
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)
    star_names = []
    distance = []
    mass = []
    radius = []
    for i in range(1,len(temp_list)):
        star_names.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])
    star_data = zip(star_names,distance,mass,radius)

    with open("data.csv", "w") as f:
        csvWritter = csv.writer(f)
        csvWritter.writerow(headers)
        csvWritter.writerows(star_data)
scrape()
