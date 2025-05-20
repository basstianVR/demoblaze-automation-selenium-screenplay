from screenpy import Actor, Eventually
from screenpy_selenium.actions import Click, Enter, AcceptAlert, Wait
from pages.contact_page import ContactPage
from pages.navbar import NavBar

class SendMessage:
    def __init__(self, email, name, message):
        self.email = email
        self.name = name
        self.message = message

    def perform_as(self, actor: Actor):
        return actor.attempts_to(
            Click.on(NavBar.CONTACT_BUTTON),
            Wait.for_the(ContactPage.EMAIL_FIELD).to_appear(),
            Enter.the_text(self.email).into_the(ContactPage.EMAIL_FIELD),
            Enter.the_text(self.name).into_the(ContactPage.NAME_FIELD),
            Enter.the_text(self.message).into_the(ContactPage.MESSAGE_FIELD),
            Click.on(ContactPage.BUTTON_SEND_MESSAGE),
            Eventually(AcceptAlert())
        )
