from actors.user import create_user
from tasks.login import LogIn
from screenpy_selenium.questions import Text
from data.users import TestUsers
from pages.navbar import NavBar
from screenpy import See
from screenpy.resolutions import ContainsTheText

def test_user_can_log_in():
    Sebas = create_user()
    
    user = TestUsers.DARKAN
    
    Sebas.attempts_to(
        LogIn(user["username"], user["password"])
    )

    Sebas.should(
        See.the(Text.of(NavBar.WELCOME_MESSAGE), ContainsTheText(f"Welcome {user["username"]}"))
    )
    

    Sebas.exit_stage_left()
