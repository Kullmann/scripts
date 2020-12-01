from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://pccables.com/")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("usb")
search.send_keys(Keys.RETURN)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mastergrid"))
    )
    items = driver.find_elements_by_class_name("img")
    for item in items:
        print(item.text)
except:
    driver.quit()


# print(driver.page_source)
# print(main.text)
# time.sleep(5)
# print(search)

driver.quit()
