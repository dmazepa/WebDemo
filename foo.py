# foo.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import chromedriver_binary
import os
os.chmod('./chromedriver', 0o755)
path = os.getenv('PATH');
print(path);
ser = Service('./chromedriver')
op = webdriver.ChromeOptions()
op.add_argument('--headless')
driver = webdriver.Chrome(service=ser, options=op)

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()