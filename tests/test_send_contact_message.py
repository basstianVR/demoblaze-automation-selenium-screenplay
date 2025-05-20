from actors.user import create_user
from tasks.login import LogIn
from tasks.send_messege import SendMessage
from screenpy_selenium.questions import Text
from pages.navbar import NavBar
from screenpy import See
from screenpy.resolutions import ContainsTheText

def test_send_contact_message():
    Sebas = create_user()

    Sebas.attempts_to(
        LogIn("Darkan", "pwd1234"),
        SendMessage("example@gmail.com", "Chris Smith", "I need a discount")
    )