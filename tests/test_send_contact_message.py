from actors.user import create_user
from data.users import TestUsers
from data.contact import ContactInfo
from tasks.login import LogIn
from tasks.send_message import SendMessage

def test_send_contact_message():
    Sebas = create_user()
    user = TestUsers.DARKAN
    messageInfo = ContactInfo.CONTACT_INFO_1

    Sebas.attempts_to(
        LogIn(user["username"],user["password"]),
        SendMessage(messageInfo["email"], messageInfo["name"], messageInfo["message"])
    )

    Sebas.exit_stage_left()