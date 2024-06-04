from selenium import webdriver
from selenium.webdriver.common.by import By
import os

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Set up Chrome WebDriver (make sure to have chromedriver installed and its location in PATH)
driver = webdriver.Chrome()

# URL of the website
url = "https://thispersondoesnotexist.com/"

# Open the URL
driver.get(url)

# Find the image element
image_element = driver.find_element(By.TAG_NAME, "img")

# Extract the image URL
image_url = image_element.get_attribute("src")

# Create a directory to store the images if it doesn't exist
create_directory("images")

i = 0
while(True and i < 100000):
    # Download the image
    image_filename = "images/" + str(i) + ".jpg"
    driver.get(image_url)
    with open(image_filename, 'wb') as f:
        f.write(driver.find_element(By.TAG_NAME, 'img').screenshot_as_png)
    i += 1

# Close the WebDriver
driver.quit()