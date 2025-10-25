from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = "http://suninjuly.github.io/simple_form_find_task.html"

try:

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    # Укажи путь к драйверу
    service = Service("C:/yandexdriver.exe")

    # Создаём браузер (он откроет Яндекс)
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
