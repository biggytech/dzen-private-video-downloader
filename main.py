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
FILE_EXTENSTION = "mp4"

# CSS selectors
USER_PROFILE_BUTTON = "button[class*=\"dzen-layout--avatar__isButton\"]"
VIDEO_PLAYER = "video"
VIDEO_TITLE = "[class*=\"video-header__title\"]"

# JS selectors
JS_VIDEO_URL_EXTRACT = "window?.YandexZen?.VideoPlayerBundle?.videoPlayersManager?.players?.[0]?.convertedStreams?.MPEG?.['Invariant quality']"

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

    print("Waiting for video page to load (You may need to focus on the browser window)...")

    # wait till page opens
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, VIDEO_PLAYER))
    )

    title_element = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, VIDEO_TITLE))
    )
    title = title_element.text

    download_url = driver.execute_script('''
        const url = {JS_VIDEO_URL_EXTRACT} ?? null;
        console.log('URL!', url);
        return url;
    '''.format(JS_VIDEO_URL_EXTRACT=JS_VIDEO_URL_EXTRACT))

    if not download_url:
        print("Can't retrieve video download url. Skipping...")
        continue

    print("Title: " + title)
    print("Download url: " + download_url)

    file_name = title + "." + FILE_EXTENSTION

    print("Download started (in the browser)...")

    driver.get(download_url)

