from actors.user import create_user
from tasks.login import LogIn
from screenpy_selenium.questions import Text
from pages.login_page import LoginPage

def test_user_can_log_in():
    Sebas = create_user()
    
    Sebas.attempts_to(
        LogIn("Darkan", "pwd1234")  # replace with your demo credentials
    )

    Sebas.should_see_the(
        (Text.of(LoginPage.LOGGED_IN_USER), lambda t: "Welcome" in t)
    )

    Sebas.exit_stage_left()
