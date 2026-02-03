from pathlib import Path


from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver.exe'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-allow-origins=*")


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    chrome_services = Service(executable_path=str(CHROMEDRIVER_PATH))
    browser = webdriver.Chrome(service=chrome_services, options=chrome_options)
    return browser


if __name__ == '__main__':
    browser = make_chrome_browser('--headless')
    browser.get('http://www.udemy.com')
    sleep(5)
    browser.quit()




