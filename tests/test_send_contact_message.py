from actors.user import create_user
from tasks.login import LogIn
from tasks.send_message import SendMessage

def test_send_contact_message():
    Sebas = create_user()

    Sebas.attempts_to(
        LogIn("Darkan", "pwd1234"),
        SendMessage("example@gmail.com", "Chris Smith", "I need a discount")
    )