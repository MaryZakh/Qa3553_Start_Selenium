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

    print(button.tag_name)
    print(button.text)

    print(button_1.tag_name)
    print(button_1.text)

    links = driver.find_elements(By.TAG_NAME, "a")
    links_1 = driver.find_elements(By.CSS_SELECTOR, "a")
    print(len(links))
    for link in links:
        print(link.text)

    print(len(links_1))
    for link in links_1:
        print(link.text)

    # by class

    container = driver.find_element(By.CLASS_NAME, "container")
    container_1 = driver.find_element(By.CSS_SELECTOR, ".container")

    print("container class: ", container.get_attribute("class"))
    print("container_1 class: ", container_1.get_attribute("class"))

    # by id

    nav = driver.find_element(By.ID, "nav")
    nav_1 = driver.find_element(By.CSS_SELECTOR, "#nav")

    print("NAV id: ", nav.tag_name)
    print("NAV id: ", nav_1.tag_name)

    # by attribute

    name_input = driver.find_element(By.CSS_SELECTOR, "[placeholder='Type your name']")
    item_2 = driver.find_element(By.CSS_SELECTOR, "[href='#item2']")
    nav_2 = driver.find_element(By.CSS_SELECTOR, "[id = 'nav']")

    input_name = driver.find_element(By.CSS_SELECTOR, "[name = 'name']")
    input_name_1 = driver.find_element(By.NAME, "name")

    input =driver.find_element(By.CSS_SELECTOR,"[placeholder = 'Type your name']")
    starts_input = driver.find_element(By.CSS_SELECTOR,"[placeholder ^= 'Type']")
    ends_input = driver.find_element(By.CSS_SELECTOR, "[placeholder $= 'name']")
    contains_input = driver.find_element(By.CSS_SELECTOR, "[placeholder *= 'your']")


#linkText & partialLinkText

    item1 = driver.find_element(By.LINK_TEXT,"Item 1")
    all_items = driver.find_elements(By.PARTIAL_LINK_TEXT, "Item")



    first_child = driver.find_element(By.CSS_SELECTOR,"li:first-child")
    last_child = driver.find_element(By.CSS_SELECTOR,"li:last-child")
    nth_child = driver.find_element(By.CSS_SELECTOR,"li:nth-child(2)")
    #nth_child_1 = driver.find_element(By.CSS_SELECTOR, "li:nth-child(1)")


#Canada
    canada = driver.find_element(By.CSS_SELECTOR,"tr:nth-child(3)>td:last-child")
    assert canada.text == "Canada"

# input("Press Enter to close the browser...")
finally:
# driver.close()
    driver.quit()
