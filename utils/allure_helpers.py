import allure


def attach_screenshot(page, name: str = "Screenshot", full_page: bool = True, timeout: int = 5000) -> None:
    """Скриншот с кастомным таймаутом."""
    try:
        allure.attach(
            page.screenshot(full_page=full_page, timeout=timeout),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        # Фоллбэк: пробуем сделать скриншот только видимой области
        try:
            allure.attach(
                page.screenshot(full_page=False, timeout=timeout),
                name=f"{name} (visible area only)",
                attachment_type=allure.attachment_type.PNG
            )
        except Exception:
            # Если совсем не получается, логируем ошибку
            allure.attach(
                f"Failed to capture screenshot: {str(e)}",
                name=f"{name} ERROR",
                attachment_type=allure.attachment_type.TEXT
            )


def attach_page_source(page, name: str = "Page Source", timeout: int = 5000) -> None:
    """HTML-код страницы с таймаутом."""
    try:
        allure.attach(
            page.content(),
            name=name,
            attachment_type=allure.attachment_type.HTML
        )
    except Exception as e:
        allure.attach(
            f"Failed to get page source: {str(e)}",
            name=f"{name} ERROR",
            attachment_type=allure.attachment_type.TEXT
        )


def attach_text_log(content: str, name: str = "Log") -> None:
    """Текстовый лог."""
    allure.attach(
        content,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )
