from actors.user import create_user
from tasks.login import LogIn
from tasks.add_to_cart import AddItemToCart
from screenpy_selenium.questions import Text
from screenpy_selenium.actions import Pause
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

    Sebas.attempts_to(
        AddItemToCart("Samsung galaxy s6")
    )
    

    Sebas.exit_stage_left()