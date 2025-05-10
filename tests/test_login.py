from actors.user import create_user
from tasks.login import LogIn
from screenpy_selenium.questions import Text
from pages.navbar import NavBar
from screenpy import See
from screenpy.resolutions import ContainsTheText

def test_user_can_log_in():
    Sebas = create_user()
    
    Sebas.attempts_to(
        LogIn("Darkan", "pwd1234")
    )

    Sebas.should(
        See.the(Text.of(NavBar.WELCOME_MESSAGE), ContainsTheText("Welcome Darkan"))
    )
    

    Sebas.exit_stage_left()
