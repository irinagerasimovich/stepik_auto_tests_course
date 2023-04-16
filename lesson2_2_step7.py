from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os 


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
url_start = "http://suninjuly.github.io/file_input.html"

try:
    # Запуск браузера с доп. опциями
    browser = webdriver.Chrome(options=options)
    browser.get(url_start)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Ivan")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Petrov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("email@gmail.com")
    
    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname("e:\selenium_course\lesson2_2_step7.py"))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)

# Отправляем заполненную форму
    #button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()
#browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    time.sleep(10)
    browser.quit()
