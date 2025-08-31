from playwright.sync_api import sync_playwright, expect, Page
import pytest
@pytest.mark.regression
@pytest.mark.registration
def test_successgul_registration(chromium_page: Page):
      # Переходим на страницу входа
        chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем поле email
        email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        # Заполняем поле Username
        username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("username")

        # Заполняем поле пароль
        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

        # Проходим регистрацию
        registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_visible()
        registration_button.click()

        #  Проверяем наличие заголовка Dashboar
        dashboard = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard).to_be_visible()