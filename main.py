import time
from login import login_start
from selenium_config import driver
from task_one import task_one
from task_two import task_two
from task_three import task_three

# Main url
url_to_open = 'https://office.birdarcha.uz/'
driver.get(url_to_open)

try:
    login_start()

    time.sleep(5)
    task_one()

    time.sleep(5)
    task_two()

    time.sleep(5)
    task_three()

except Exception as e:
    print(f"An error occurred: {str(e)}")

time.sleep(2000000)
driver.quit()
