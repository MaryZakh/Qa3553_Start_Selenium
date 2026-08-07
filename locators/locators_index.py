# var1
# page_url = "file:///C:/Users/marii/Downloads/21.index.html"
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By

html_file = Path(__file__).parent / "21.index.html"
page_url = html_file.as_uri()

driver = webdriver.Chrome()

try:
    driver.get(page_url)

    # by tag_name
    button = driver.find_element(By.TAG_NAME, "button")
    button_1 = driver.find_element(By.CSS_SELECTOR, "button")
    button_2 = driver.find_element(By.XPATH, "//button")

    links = driver.find_elements(By.TAG_NAME, "a")
    links_1 = driver.find_elements(By.CSS_SELECTOR, "a")
    links_3 = driver.find_elements(By.XPATH, "//a")

    # by class

    container = driver.find_element(By.CLASS_NAME, "container")
    container_1 = driver.find_element(By.CSS_SELECTOR, ".container")
    container_2 = driver.find_element(By.XPATH, "//div[@class='container']")
    container_3 = driver.find_element(By.XPATH, "//*[@class='container']")

    # by id

    nav = driver.find_element(By.ID, "nav")
    nav_1 = driver.find_element(By.CSS_SELECTOR, "#nav")
    nav_2 = driver.find_element(By.XPATH, "//*[@id='nav']")

    # by attribute

    name_input = driver.find_element(By.CSS_SELECTOR, "[placeholder='Type your name']")
    name_input_1 = driver.find_element(By.XPATH, "//*[@placeholder = 'Type your name']")

    item_2 = driver.find_element(By.CSS_SELECTOR, "[href='#item2']")
    item_3 = driver.find_element(By.XPATH, "//*[@href='#item2']")

    nav_2 = driver.find_element(By.CSS_SELECTOR, "[id = 'nav']")

    input_name = driver.find_element(By.CSS_SELECTOR, "[name = 'name']")
    input_name_1 = driver.find_element(By.NAME, "name")
    input_name_2 = driver.find_element(By.XPATH, "//*[@name='name']")

    input = driver.find_element(By.CSS_SELECTOR, "[placeholder = 'Type your name']")
    input_xPath = driver.find_element(By.XPATH, "//*[@placeholder='Type your name']")

    starts_input = driver.find_element(By.CSS_SELECTOR, "[placeholder ^= 'Type']")
    starts_input_xPath = driver.find_element(By.XPATH, "//input[starts-with(@placeholder,'Type')]")

    ends_input = driver.find_element(By.CSS_SELECTOR, "[placeholder $= 'name']")
    ends_input_xPath = driver.find_element(By.XPATH, "//*[contains(@placeholder,'name')]")

    contains_input = driver.find_element(By.CSS_SELECTOR, "[placeholder *= 'your']")
    contains_input_xPath = driver.find_element(By.XPATH, "//*[contains(@placeholder,'your')]")

    # linkText & partialLinkText

    item1 = driver.find_element(By.LINK_TEXT, "Item 1")
    all_items = driver.find_elements(By.PARTIAL_LINK_TEXT, "Item")

    first_child = driver.find_element(By.CSS_SELECTOR, "li:first-child")
    last_child = driver.find_element(By.CSS_SELECTOR, "li:last-child")
    last_child_1 = driver.find_element(By.XPATH,"//li[last()]")

    nth_child = driver.find_element(By.CSS_SELECTOR, "li:nth-child(2)")
    # nth_child_1 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(1)")
    nth_child_1 = driver.find_element(By.XPATH,"//li[2]")

    # Canada
    canada = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3)>td:last-child")
    assert canada.text == "Canada"

    canada_text = driver.find_element(By.XPATH, "//*[text()='Canada']")

# input("Press Enter to close the browser...")
finally:
    # driver.close()
    driver.quit()
