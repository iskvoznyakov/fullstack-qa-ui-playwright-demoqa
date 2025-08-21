from pages.base_page import BasePage
from config import BASE_URL

class TextBoxPage(BasePage):
    FULL_NAME_FIELD = "#userName"
    EMAIL_FIELD = "#userEmail"
    CURRENT_ADDRESS_FIELD = "#currentAddress"
    PERMANENT_ADDRESS_FIELD = "#permanentAddress"
    SUBMIT_BUTTON = "#submit"
    OUTPUT_FIELD = "#output"

    def open(self):
        super().navigate(BASE_URL + "/text-box")

    def fill_the_form(self, full_name, email, current_address, permanent_address):
        self.input_text(self.FULL_NAME_FIELD, full_name)
        self.input_text(self.EMAIL_FIELD, email)
        self.input_text(self.CURRENT_ADDRESS_FIELD, current_address)
        self.input_text(self.PERMANENT_ADDRESS_FIELD, permanent_address)
        self.click(self.SUBMIT_BUTTON)

    def get_output(self):
        if not self.is_visible(self.OUTPUT_FIELD):
            raise AssertionError("Поле вывода не отображается — нельзя получить данные")

        output_dict = {}

        output_elements = self.page.locator("#output *").all_text_contents()

        for element_text in output_elements:
            if ':' in element_text:
                key, value = element_text.split(':', 1)
                output_dict[key.strip()] = value.strip()

        return output_dict

    def is_visible_output_field(self):
        output_text = self.get_text(self.OUTPUT_FIELD)
        return bool(output_text and output_text.strip())