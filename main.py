# import webbrowser
# import sys
#
URL = 'https://dzen.ru/'
#
# if not webbrowser.open(URL, new=2):
#     print("Couldn't open browser window. Exiting...")
#     sys.exit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Opening " + URL + "...")

# This will open chrome browser
driver = webdriver.Chrome()
driver.get(URL)

print("Please, authenticate in " + URL + " for further work")
print("Waiting for user authentication...")

# Now wait for me to manually load a page, and look for the CSS selector.
user_profile_button = WebDriverWait(driver, 300).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "button[class*=\"dzen-layout--avatar__isButton\"]"))
)

print("User successfully authenticated!")

# # Once the selector is found, it will grab the `id` attribute and print it
# text_input = element.get_attribute("id")
# print(text_input)
