from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the CoWIN website
driver.get("https://www.cowin.gov.in/")

# Wait for the page to load
time.sleep(5)

# Find and click on the "FAQ" link
faq_link = driver.find_element(By.LINK_TEXT, "FAQ")
faq_link.click()
time.sleep(2)

# Find and click on the "Partners" link
partners_link = driver.find_element(By.LINK_TEXT, "Partners")
partners_link.click()
time.sleep(2)

# Get all window handles
window_handles = driver.window_handles
print("Window Handles:", window_handles)

# Close all windows except the original one
original_window = driver.current_window_handle
for handle in window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        driver.close()

# Switch back to the original window
driver.switch_to.window(original_window)
print("Returned to the home page")

# Close the browser
driver.quit()
