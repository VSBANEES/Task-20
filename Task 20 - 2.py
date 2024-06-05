import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Labour Ministry website
driver.get("https://labour.gov.in/")

# Wait for the page to load
time.sleep(5)

# Task 2.1: Download Monthly Progress Report
documents_menu = driver.find_element(By.XPATH, "//a[text()='Documents']")
documents_menu.click()
time.sleep(2)

monthly_progress_report = driver.find_element(By.XPATH, "//a[text()='Monthly Progress Report']")
monthly_progress_report.click()
time.sleep(2)

# Find the link to download the report (assuming the link text is 'Download')
download_link = driver.find_element(By.LINK_TEXT, "Download")
report_url = download_link.get_attribute('href')
report_response = requests.get(report_url)

# Save the report
with open('Monthly_Progress_Report.pdf', 'wb') as file:
    file.write(report_response.content)

print("Monthly Progress Report downloaded")

# Task 2.2: Download 10 photos from Photo Gallery
media_menu = driver.find_element(By.XPATH, "//a[text()='Media']")
media_menu.click()
time.sleep(2)

photo_gallery_menu = driver.find_element(By.XPATH, "//a[text()='Photo Gallery']")
photo_gallery_menu.click()
time.sleep(2)

# Create a folder to save photos
os.makedirs('Photo_Gallery', exist_ok=True)

# Find the first 10 image elements and download the images
images = driver.find_elements(By.XPATH, "//img[@class='img-responsive']")[:10]
for idx, img in enumerate(images):
    img_url = img.get_attribute('src')
    img_response = requests.get(img_url)
    with open(f'Photo_Gallery/photo_{idx + 1}.jpg', 'wb') as file:
        file.write(img_response.content)
    print(f"Downloaded photo {idx + 1}")

# Close the browser
driver.quit()
