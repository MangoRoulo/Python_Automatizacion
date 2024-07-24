# Paquetes importados
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Inciio de Chrome
# path = Service("C:\Users\steve\OneDrive\Desktop\Python\Drivers\chromedriver-win64\chromedriver.exe")
path = Service(r"C:\Users\steve\OneDrive\Desktop\Python\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=path)
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)


# Campos
Name = "(//input[contains(@autocomplete,'off')])[1]"
Email = "(//input[contains(@autocomplete,'off')])[2]"
Adress = "//textarea[contains(@id,'currentAddress')]"
PermanentAdress = "//textarea[contains(@id,'permanentAddress')]"
submit = "//button[contains(@id,'submit')]" 

# Página Web
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

# Acciones
driver.find_element(By.XPATH, Name).send_keys("Steven")
time.sleep(2)   
driver.find_element(By.XPATH, Email).send_keys("sarias@colegium.com")
time.sleep(2)   
driver.find_element(By.XPATH, Adress).send_keys("Calle 38")
time.sleep(2)  
driver.find_element(By.XPATH, PermanentAdress).send_keys("# 24b - 185")
time.sleep(2)  
driver.find_element(By.XPATH, submit).click()
time.sleep(2)  

# Cerrar el navegador
driver.quit()   

#prueba de cambio