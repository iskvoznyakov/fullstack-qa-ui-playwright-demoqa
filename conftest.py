import pytest
from playwright.sync_api import sync_playwright
from utils.allure_helpers import attach_screenshot, attach_page_source


@pytest.fixture(scope="function")
def page():
    """Фикстура для создания страницы Playwright."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False,
            slow_mo=500,
            args=["--incognito"]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page")
        if page:
            attach_screenshot(page, name="Failure Screenshot")
            attach_page_source(page, name="Failure Page Source")