from pages.checkbox_page import CheckBoxPage
import pytest


@pytest.mark.parametrize("checkbox_name", [
    "Notes", "React", "Public"
])
def test_select_one_checkbox(page, checkbox_name):
    check_box_page = CheckBoxPage(page)
    check_box_page.open()
    check_box_page.expand_all_the_checkboxes()
    check_box_page.click_checkbox_by_name(checkbox_name)
    assert check_box_page.is_checkbox_selected(checkbox_name), f"Чек-бокс {checkbox_name} не был выбран"
