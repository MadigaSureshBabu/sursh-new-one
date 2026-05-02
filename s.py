from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

# Setup Edge options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0")

# Launch Edge browser
driver = webdriver.Edge(options=options)

# Open Google
driver.get("https://www.google.com")
driver.maximize_window()

time.sleep(3)

# Find search box and enter text
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Web Testing")

time.sleep(2)

# Press Enter
search_box.send_keys(Keys.RETURN)

time.sleep(5)

print("Page loaded successfully")

# Close browser
driver.quit()