from actors.user import create_user
from tasks.login import LogIn
from tasks.log_out import LogOut
from screenpy_selenium.questions import Text
from data.users import TestUsers
from pages.navbar import NavBar
from screenpy import See, Eventually
from screenpy.resolutions import ContainsTheText

def test_log_out():
    Sebas = create_user()

    user = TestUsers.DARKAN
    
    Sebas.attempts_to(
        LogIn(user["username"], user["password"])
    )

    Sebas.should(
        See.the(Text.of(NavBar.WELCOME_MESSAGE), ContainsTheText(f"Welcome {user["username"]}"))
    )

    Sebas.attempts_to(
        LogOut()
    )

    Sebas.should(
        Eventually(See.the(Text.of(NavBar.LOGIN_NAV_BUTTON), ContainsTheText("Log in")))
    )