from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# Set the path to Edge WebDriver
service = Service("C:/webdriver/msedgedriver.exe")  # change path if needed

# Launch Edge browser
driver = webdriver.Edge(service=service)

# Open Google
driver.get("https://www.facebook.com")

time.sleep(2)

# Find search box
search_box = driver.find_element(By.NAME, "q")

# Print element
print("Search box element found:", search_box)

# Close browser
driver.quit()