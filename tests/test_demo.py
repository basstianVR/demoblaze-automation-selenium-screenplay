import pytest
from actors.user import create_user
from tasks.login import LogIn
from tasks.add_to_cart import AddItemToCart
from tasks.select_item import SelectItem
from tasks.go_to_cart import GoToCart
from tasks.delete_item import DeleteItem
from tasks.send_message import SendMessage
from tasks.log_out import LogOut
from screenpy_selenium.questions import Text
from data.products import ProductNames
from data.users import TestUsers
from data.contact import ContactInfo
from pages.navbar import NavBar
from pages.info_item_page import InfoItemPage
from pages.cart_page import CartPage
from screenpy_selenium.actions import Wait
from screenpy import Eventually, See, Pause
from screenpy.resolutions import ContainsTheText

@pytest.fixture(scope="module")
def user():
    Sebas = create_user()
    yield Sebas
    Sebas.exit_stage_left()

def test_user_can_log_in(user):
    
    account = TestUsers.DARKAN
    
    user.attempts_to(
        LogIn(account["username"], account["password"])
    )

    user.should(
        See.the(Text.of(NavBar.WELCOME_MESSAGE), ContainsTheText(f"Welcome {account["username"]}"))
    )

def test_add_item_to_car(user):
    
    user.attempts_to(
        SelectItem(ProductNames.PRODUCT_PHONE_NAMES[0])
    )

    user.should(
        Eventually(See.the(Text.of(InfoItemPage.TITLE_ITEM), ContainsTheText(ProductNames.PRODUCT_PHONE_NAMES[0])))
    )

    user.attempts_to(
        AddItemToCart(),
        GoToCart(),
    )

    user.should(
        Eventually(See.the(Text.of(CartPage.LAST_ITEM_ADDED), ContainsTheText(ProductNames.PRODUCT_PHONE_NAMES[0])))
    )

def test_delete_item(user):

    user.attempts_to(
        DeleteItem(CartPage.DELETE_BUTTON)
    )

def test_send_contact_message(user):

    messageInfo = ContactInfo.CONTACT_INFO_1

    user.attempts_to(
        Pause.for_(0.5).seconds_because("Need time"),
        SendMessage(messageInfo["email"], messageInfo["name"], messageInfo["message"])
    )

def test_log_out(user):
    
    user.attempts_to(
        Pause.for_(0.5).seconds_because("Need time"),
        LogOut()
    )

    user.should(
        See.the(Text.of(NavBar.LOGIN_NAV_BUTTON), ContainsTheText("Log in"))
    )