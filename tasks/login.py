from screenpy import Actor
from screenpy_selenium.actions import Open, Click, Enter, Wait
from pages.login_page import LoginPage
from pages.navbar import NavBar

class LogIn:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def perform_as(self, actor: Actor):
        return actor.attempts_to(
            Open.browser_on(LoginPage.URL),
            Click.on(NavBar.LOGIN_NAV_BUTTON),
            Wait.for_the(LoginPage.USERNAME_INPUT).to_appear(),
            Enter.the_text(self.username).into(LoginPage.USERNAME_INPUT),
            Enter.the_text(self.password).into(LoginPage.PASSWORD_INPUT),
            Click.on(LoginPage.SUBMIT_LOGIN_BUTTON),
            Wait.for_the(NavBar.WELCOME_FIELD).to_appear()
        )
