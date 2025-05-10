from screenpy import Actor
from screenpy_selenium.actions import Open, Click, Enter, Wait
from screenpy_selenium.questions import Text
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

class LogIn:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def perform_as(self, actor: Actor):
        return actor.attempts_to(
            Open.browser_on(LoginPage.URL),
            Click.on(LoginPage.LOGIN_NAV_BUTTON),
            Wait.for_the(LoginPage.USERNAME_INPUT).to_appear(),
            Enter.the_text(self.username).into(LoginPage.USERNAME_INPUT),
            Enter.the_text(self.password).into(LoginPage.PASSWORD_INPUT),
            Click.on(By.XPATH,LoginPage.SUBMIT_LOGIN_BUTTON)
        )
