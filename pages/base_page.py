from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    def input_text(self, selector: str, text: str) -> None:
        self.page.locator(selector).fill(text)

    def is_visible(self, selector: str, timeout: float = 10.0) -> bool:
        try:
            expect(self.page.locator(selector)).to_be_visible(timeout=timeout * 1000)
            return True
        except PlaywrightTimeoutError:
            return False

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content()

    def scroll_to_element(self, selector: str) -> None:
        self.page.locator(selector).scroll_into_view_if_needed()
