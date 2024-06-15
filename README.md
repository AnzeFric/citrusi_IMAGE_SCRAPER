# citrusi_IMAGE_SCRAPER

## Overview

This image scraper is a for a college project, where we later used the images in machine learning for faceID and 2FA. It is a Python script that uses Selenium WebDriver to automate the process of downloading images from the website [This Person Does Not Exist](https://thispersondoesnotexist.com/). The script opens the website, extracts the image URL, and saves the image to a specified directory. By default, it downloads 10 images.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver
- Google Chrome Browser

## Installation

1. **Install Python:** Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Selenium:** Install the Selenium package using pip:
    ```sh
    pip install selenium
    ```

3. **Download Chrome WebDriver:**
    - Download the Chrome WebDriver from the official site: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    - Ensure that the downloaded `chromedriver` is in your system PATH. You can also place it in the same directory as your script.

## Usage

1. **Clone or Download the Script:**
    Download the script to your local machine.

2. **Run the Script:**
    Open a terminal or command prompt and navigate to the directory containing the script. Run the script using Python:
    ```sh
    python image_scraper.py
    ```

3. **Output:**
    The script will create a directory named `images` in the same directory as the script and save the downloaded images as `0.jpg`, `1.jpg`, ..., `9.jpg`.

## Script Explanation

Here is a breakdown of what the script does:

1. **Imports Required Libraries:**
    ```python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import os
    ```

2. **Function to Create a Directory:**
    ```python
    def create_directory(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
    ```

3. **Set Up Chrome WebDriver:**
    ```python
    driver = webdriver.Chrome()
    ```

4. **Open the URL and Find the Image Element:**
    ```python
    url = "https://thispersondoesnotexist.com/"
    driver.get(url)
    image_element = driver.find_element(By.TAG_NAME, "img")
    image_url = image_element.get_attribute("src")
    ```

5. **Create a Directory to Store Images:**
    ```python
    create_directory("images")
    ```

6. **Download Images in a Loop:**
    ```python
    i = 0
    while(True and i < 10):
        image_filename = "images/" + str(i) + ".jpg"
        driver.get(image_url)
        with open(image_filename, 'wb') as f:
            f.write(driver.find_element(By.TAG_NAME, 'img').screenshot_as_png)
        i += 1
    ```

7. **Close the WebDriver:**
    ```python
    driver.quit()
    ```

## Notes

- Ensure that the Chrome WebDriver version matches your installed Google Chrome version.
- You can adjust the number of images to download by changing the condition in the `while` loop.
- The script uses `screenshot_as_png` to save the images. This approach captures the image displayed in the browser. If the website changes its structure, you might need to update the selector used to find the image element.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests for any improvements or additional features. 
