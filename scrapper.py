from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd

url_list = pd.read_excel('/home/yash/project/interview-tasks/Delivery-Scraping/Documents/E-commerce URL.xlsx')
print(url_list)