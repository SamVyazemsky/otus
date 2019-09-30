from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



wd = webdriver.Chrome()
wd.set_page_load_timeout(10)
wd.implicitly_wait(10)
wd.get("https://pagination.js.org/")
el = wd.find_element_by_css_selector('div.data-container ul li')
ul = wd.find_elements_by_css_selector("div.paginationjs-pages ul li")
ul[3].click()
button = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.data-container ul li')))
button.click()
excluted_button = WebDriverWait(wd, 10).until(EC.staleness_of(button))
button = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.ID, 'id')))

print(wait.text)

