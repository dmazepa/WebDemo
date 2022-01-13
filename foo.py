# foo.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

ser = Service(ChromeDriverManager().install())
op = webdriver.ChromeOptions()
op.add_argument("window-size=1920x1480")
op.add_argument("disable-dev-shm-usage")
op.add_argument("headless")
op.add_argument('--headless')
op.add_argument('--no-sandbox')
op.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', service=ser, options=op)



s=Service('C:/Users/Morteza/Documents/Dev/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='https://www.google.com'
browser.get(url)


driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()