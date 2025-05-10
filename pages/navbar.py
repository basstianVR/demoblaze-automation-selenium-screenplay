from selenium.webdriver.common.by import By
from screenpy_selenium import Target

class NavBar:
    LOGIN_NAV_BUTTON = Target.the("login nav button").located_by((By.ID, "login2"))
    WELCOME_FIELD = Target.the("welcome field").located_by((By.XPATH, "//a[@id='nameofuser']"))
    WELCOME_MESSAGE = Target.the("welcome message").located((By.ID, "nameofuser"))