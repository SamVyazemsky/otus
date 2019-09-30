
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

"""
Если изначальный сайт получится открыть.. вероятно требуется переписать поиск элементов из driver  на framebox из коммента
frame_box = driver.find_element_by_xpath("/html/body/div/article/div/div/iframe[1][@src='https://marcojakob.github.io/dart-dnd/basic/']")
"""

driver = webdriver.Chrome()
driver.get("https://marcojakob.github.io/dart-dnd/basic/")
doc = driver.find_elements_by_class_name("document")
trash = driver.find_element_by_class_name("trash")
for d in doc:
    ActionChains(driver).pause(1).move_to_element(d).click_and_hold().move_to_element(trash).release().perform()
driver.quit()