from selenium import webdriver
from selenium.webdriver.edge import service
from fake_useragent import UserAgent
import time
import os
os.system("cls")

PROXY = "149.14.242.202:9999"
webdriver.DesiredCapabilities.EDGE['proxy'] = {
    "httpProxy" : PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
}

def User():
    
    ua = UserAgent()
    #ua = "test3 user-agent"
    return ua.random


edgeOption = webdriver.EdgeOptions()
edgeOption.add_argument(f'user-agent={User()}')
#edgeOption.use_chromium = True
edgeOption.add_argument("start-maximized")
#edgeOption.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
s=service.Service(r'msedgedriver.exe')
driver = webdriver.Edge(service=s, options=edgeOption)
driver.get("http://whatsmyuseragent.org/")
time.sleep(3)