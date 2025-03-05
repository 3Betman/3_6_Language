from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket(browser):
    browser.get(link)
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket")))
    assert button.is_displayed(), "Button is not visible!"
