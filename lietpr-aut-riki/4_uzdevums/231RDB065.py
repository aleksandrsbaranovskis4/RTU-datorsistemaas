import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
from openpyxl import Workbook, load_workbook 

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

name=[]
# program read information from people.csv file and put all data in name list.
with open("people.csv", "r") as file:
    next(file)
    for line in file:
        row=line.rstrip().split(",") 
        name.append(row)

url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
elem = driver.find_element(By.ID, "input")
for row in name:
    input = f"{row[2]} {row[3]}"
    elem.send_keys(input)
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element(By.ID, "execute")
    elem.send_keys(Keys.LEFT)
    elem = driver.find_element(By.ID, "output")
    