import pytest
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_log_in_passed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("6531testowanieselenium@testers.pl", "testowanieselenium")

        assert my_account_page.is_logout_link_displayed()

    def test_log_in_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.log_in("6531testowanieselenium@testers.pl123", "testowanieselenium123")

        assert "ERROR: Incorrect username or password." in my_account_page.get_error_msg()



