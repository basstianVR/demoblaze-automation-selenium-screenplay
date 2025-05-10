from selenium.webdriver.common.by import By
from screenpy_selenium import Target

class LoginPage:
    URL = "https://www.demoblaze.com/index.html"
    USERNAME_INPUT = Target.the("username input").located_by((By.ID, "loginusername"))
    PASSWORD_INPUT = Target.the("password input").located_by((By.ID, "loginpassword"))
    SUBMIT_LOGIN_BUTTON = Target.the("submit login button").located_by((By.XPATH, "//button[text()='Log in']"))