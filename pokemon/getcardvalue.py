from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


driver.get("https://mavin.io/")


def pokemonValueMavin(fullCardDesc):
    search = driver.find_element_by_name("q")
    search.send_keys(fullCardDesc)
    search.send_keys(Keys.RETURN)
    try:
        estimateBox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "estimate-box"))
        )
        cardValue = estimateBox.find_element_by_tag_name('h4')
    except:
        driver.quit()
    driver.find_element_by_name("q").clear()
    return cardValue.text


def exitBrowser():
    driver.quit()
