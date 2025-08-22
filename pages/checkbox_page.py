from config import BASE_URL
from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    RESULT_FIELD = "#result .text-success"
    EXPAND_ALL_BUTTON = "//button[@title='Expand all']"

    def open(self):
        super().navigate(BASE_URL + "/checkbox")

    def expand_all_the_checkboxes(self):
        self.click(self.EXPAND_ALL_BUTTON)

    def click_checkbox_by_name(self, name: str):
        checkbox_locator = f"//label[.//span[text()='{name}']]"
        self.click(checkbox_locator)

    def _get_selected_items(self):
        if not self.page.locator("#result").is_visible():
            return []

        if not self.page.locator(self.RESULT_FIELD).is_visible():
            return []

        selected_elements = self.page.locator(self.RESULT_FIELD).all_text_contents()
        return [item.strip().lower() for item in selected_elements if item.strip()]

    def is_checkbox_selected(self, checkbox):
        return checkbox.lower() in self._get_selected_items()

    def are_checkboxes_selected(self, checkboxes: list):
        selected = self._get_selected_items()
        return all(checkbox.lower() in selected for checkbox in checkboxes)
