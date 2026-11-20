from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome()

navegador.get("https://www.google.com")

pesquisa = navegador.find_element(By.NAME, "q")

pesquisa.send_keys("Python Selenium")
pesquisa.send_keys(Keys.ENTER)

time.sleep(5)

navegador.quit()