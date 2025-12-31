from data_ import Credentials
from curl import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:
    # Проверка возможности входа по кнопке "Login" 
    def test_login_from_main_site(self, driver):
        driver.get(Url.main_site)
       
        driver.find_element(*Locators.INPUT_IMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGO))
        assert driver.find_element(*Locators.LOGO).is_displayed()

   