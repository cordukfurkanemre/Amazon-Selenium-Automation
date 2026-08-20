from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchWindowException
import time

# stage 1: load the driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
time.sleep(2)

# stage 2: go to the homepage
driver.get("https://www.amazon.de/?th=1&psc=1&language=en")
time.sleep(1)

# stage 3: change the address
driver.find_element(By.XPATH,"//*[@id='glow-ingress-line2']").click()

time.sleep(1)
Select(driver.find_element(By.ID,'GLUXCountryList')).select_by_value("US")
time.sleep(1)


with open("asins.txt", encoding="utf-8") as file:
    asinlist = [line.strip() for line in file if line.strip()]

# stage 3: parse the page
def get_text(by, selector):
    elements = driver.find_elements(by, selector)

    if elements:
        text = elements[0].get_attribute("textContent").strip()
        if text:
            return text

    return "Not available"


for index, asin in enumerate(asinlist, start=1):
    try:
        driver.get(f"https://www.amazon.de/dp/{asin}?th=1&psc=1&language=en")
        time.sleep(1)

        title = get_text(By.ID, "productTitle")
        price = get_text(By.CSS_SELECTOR, ".a-price .a-offscreen")
        delivery = get_text(
            By.ID,
            "mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"
        )

        print(f"\n[{index}] {asin}")
        print(f"Title: {title}")
        print(f"Price: {price}")
        print(f"Delivery: {delivery}")
        print("-" * 60)

    except NoSuchWindowException:
        print("\nBrowser window closed.")
        break
driver.quit()
