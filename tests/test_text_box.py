import pytest
from pages.text_box_page import TextBoxPage


@pytest.mark.parametrize("full_name, email, current_address, permanent_address", [
    ("Ivan Ivanov", "email@mail.ru", "current address", "permanent address")
])
def test_valid_data_displays_output(page, full_name, email, current_address, permanent_address):
    text_box_page = TextBoxPage(page)
    text_box_page.open()
    text_box_page.fill_the_form(full_name, email, current_address, permanent_address)
    output_dict = text_box_page.get_output()
    assert output_dict.get("Name") == full_name, "Значение из поля 'Full Name' не отображается в поле вывода"
    assert output_dict.get("Email") == email, "Значение из поля 'Email' не отображается в поле вывода"
    assert output_dict.get(
        "Current Address") == current_address, "Значение из поля 'Current Address' не отображается в поле вывода"
    assert output_dict.get(
        "Permananet Address") == permanent_address, "Значение из поля 'Permanent Address' не отображается в поле вывода"


def test_invalid_email_prevents_output_display(page):
    text_box_page = TextBoxPage(page)
    text_box_page.open()
    text_box_page.fill_the_form("Ivan Ivanov", "not-an-email", "current_address", "permanent_address")
    assert not text_box_page.is_visible_output_field(), "Поле вывода отображается"
