from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pickle
import os
import time
import dotenv

dotenv.load_dotenv()


def add_cookies(driver: WebDriver):
    cookies_path = os.getenv('cookies_path')
    with open(cookies_path, 'rb') as file:
        cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)


def login(driver: WebDriver):
    url = 'https://indeed.com'
    driver.get(url)

    cookies_path = os.getenv('cookies_path')
    if os.path.exists(cookies_path):
        add_cookies(driver)

        menu_button = driver.find_element(By.LINK_TEXT, 'Sign in')
        menu_button.click()

    else:
        menu_button = driver.find_element(By.LINK_TEXT, 'Sign in')
        menu_button.click()

        email = os.getenv('email')
        input_email = driver.find_element(By.ID, 'ifl-InputFormField-3')
        input_email.send_keys(email)

        continue_button = driver.find_element(
            By.XPATH, '//button[@data-tn-element="auth-page-email-submit-button"]')
        continue_button.click()

        time.sleep(30)

        password = os.getenv('password')
        input_password = driver.find_element(By.NAME, '__password')
        input_password.send_keys(password)

        sign_in_button = driver.find_element(
            By.XPATH, '//button[@data-tn-element="auth-page-sign-in-password-form-submit-button"]')
        sign_in_button.click()

        time.sleep(30)
        cookies = driver.get_cookies()
        print(cookies)

        with open('cookies.pkl', 'wb') as file:
            pickle.dump(cookies, file)
