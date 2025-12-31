from selenium.webdriver.common.by import By

class Locators:

    
    # локаторы для входа:

    INPUT_IMAIL = By.XPATH, '//input[@id="user-name"]' 
    INPUT_PASSWORD = By.XPATH, '//input[@id="password"]' 
    LOGIN_BUTTON = By.XPATH, '//input[@id="login-button"]' 
    LOGO = (By.XPATH, '//div[@class="app_logo" and normalize-space(.)="Swag Labs"]')