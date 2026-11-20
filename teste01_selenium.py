from selenium import webdriver
import time

#Abrir o navegador
navegador = webdriver.Chrome()

#Abrir o site
navegador.get('https://www.google.pt')

time.sleep(5)

#fechar o navegador
navegador.quit()