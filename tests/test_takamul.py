
from pages.resources import Contact_form, Digitalproject_buttons
from data.users import test_user


def test_contact_form(browser_management):
    contact_form = Contact_form()
    contact_form.steps(test_user)

def test_contact_form_negative(browser_management):
    contact_form = Contact_form()
    contact_form.steps_negative(test_user)

def test_digitalproject_buttons(browser_management):
    digitalproject_buttons = Digitalproject_buttons()
    digitalproject_buttons.steps(test_user)