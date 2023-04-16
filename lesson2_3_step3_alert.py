from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):

    return str(math.log(abs(12*math.sin(int(x)))))


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
url_start = "http://suninjuly.github.io/alert_accept.html"

try:
    # Запуск браузера с доп. опциями
    browser = webdriver.Chrome(options=options)
    browser.get(url_start)

    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()
    print(browser.switch_to.alert.text)
    #pc.copy(browser.switch_to.alert.text.split(': ')[-1])   # сохранить в буфер


finally:
    time.sleep(4)
    browser.quit()
