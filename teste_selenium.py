from selenium import webdriver
import time

# abrir navegador
navegador = webdriver.Chrome()

# abrir site
navegador.get("https://www.google.com")

time.sleep(5)

# fechar navegador
navegador.quit()
