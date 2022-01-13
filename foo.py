# foo.py
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# gChromeOptions = webdriver.ChromeOptions()
# gChromeOptions.add_argument("window-size=1920x1480")
# gChromeOptions.add_argument("disable-dev-shm-usage")
# gDriver = webdriver.Chrome()
# gDriver.get("https://www.python.org/")
# time.sleep(3)
# gDriver.save_screenshot("my_screenshot.png")
# gDriver.close()


driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()