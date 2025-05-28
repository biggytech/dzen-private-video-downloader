from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import os.path

# Constants
URL = 'https://dzen.ru/'
COOKIES_FILE = "cookies.pkl"
EXIT_KEYWORD = "exit"

# CSS selectors
USER_PROFILE_BUTTON = "button[class*=\"dzen-layout--avatar__isButton\"]"
VIDEO_PLAYER = "[class*=\"player__videoViewerPlayer\"]"

print("Opening " + URL + "...")

# This will open chrome browser
driver = webdriver.Chrome()
driver.get(URL)

# Load saved cookies
if os.path.isfile(COOKIES_FILE):
    cookies = pickle.load(open(COOKIES_FILE, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get(URL)

print("Please, authenticate in " + URL + " for further work")
print("Waiting for user authentication...")

# Now wait for me to manually load a page, and look for the CSS selector.
WebDriverWait(driver, 300).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, USER_PROFILE_BUTTON))
)

print("User successfully authenticated!")

# Store browser cookies
pickle.dump( driver.get_cookies() , open(COOKIES_FILE,"wb"))

# Request URLs
while True:
    user_input = input("Paste video URL (enter 'exit' to exit): ")
    if user_input == EXIT_KEYWORD:
        break

    # do the stuff
    url = user_input
    driver.get(url)

    print("Waiting for video page to load...")

    # wait till opens
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, VIDEO_PLAYER))
    )

# # Once the selector is found, it will grab the `id` attribute and print it
# text_input = element.get_attribute("id")
# print(text_input)

# window.YandexZen.VideoPlayerBundle.videoPlayersManager.players[0].convertedStreams.MPEG['Invariant quality']
