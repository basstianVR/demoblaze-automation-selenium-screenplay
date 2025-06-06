import pytest
from actors.user import create_user
from tasks.login import LogIn
from tasks.add_to_cart import AddItemToCart
from tasks.select_item import SelectItem
from tasks.go_to_cart import GoToCart
from tasks.delete_item import DeleteItem
from screenpy_selenium.questions import Text
from screenpy_selenium.actions import Pause
from data.products import ProductNames
from data.users import TestUsers
from pages.navbar import NavBar
from pages.info_item_page import InfoItemPage
from pages.cart_page import CartPage
from screenpy import Eventually, See
from screenpy.resolutions import ContainsTheText

@pytest.mark.parametrize("product_name", ProductNames.PRODUCT_PHONE_NAMES)

def test_user_can_log_in(product_name):
    Sebas = create_user()
    user = TestUsers.DARKAN
    
    Sebas.attempts_to(
        LogIn(user["username"], user["password"])
    )

    Sebas.should(
        See.the(Text.of(NavBar.WELCOME_MESSAGE), ContainsTheText(f"Welcome {user["username"]}"))
    )

    Sebas.attempts_to(
        SelectItem(product_name)
    )

    Sebas.should(
        Eventually(See.the(Text.of(InfoItemPage.TITLE_ITEM), ContainsTheText(product_name)))
    )

    Sebas.attempts_to(
        AddItemToCart(),
        GoToCart(),
    )

    Sebas.should(
        Eventually(See.the(Text.of(CartPage.LAST_ITEM_ADDED), ContainsTheText(product_name)))
    )

    Sebas.attempts_to(
        DeleteItem(CartPage.DELETE_BUTTON),
        Pause.for_(2).seconds_because("need to see")
    )
    

    Sebas.exit_stage_left()