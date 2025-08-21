import pytest
from playwright.sync_api import sync_playwright
from utils.allure_helpers import attach_screenshot, attach_page_source
import logging

logger = logging.getLogger(__name__)


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
    """Хук для скриншотов в Allure при падении теста."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            try:
                attach_screenshot(page, name="FAILED Screenshot", timeout=5000)
            except Exception as e:
                logger.warning(f"Не удалось сделать скриншот при падении: {e}")

            try:
                attach_page_source(page, name="FAILED Page Source")
            except Exception as e:
                logger.warning(f"Не удалось получить page source: {e}")
