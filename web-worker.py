from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import dotenv
import time
from auth import login

dotenv.load_dotenv()

driver = webdriver.Chrome()
login(driver)

driver.get(
    'https://www.indeed.com/jobs?q=developer&l=Remote&sc=0kf%3Aattr%28DSQF7%29%3B&fromage=3')

li_elements = driver.find_elements(By.TAG_NAME, 'li')
for li in li_elements:
    print(li)
    try:
        a_element = li.find_element(By.TAG_NAME, 'a')
        a_element.click()
    except NoSuchElementException:
        print('Not found')
    time.sleep(5)
time.sleep(60)

driver.quit()
