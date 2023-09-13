from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--start-maximized')
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
)

chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_options)
