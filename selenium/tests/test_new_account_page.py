import pytest
from configs.Config import TestData
from tests.test_base import BaseTest
from pages.NewAccountPage import NewAccountPage


@pytest.mark.order(3)
class TestNewAccountPage(BaseTest):
    def test_add_account(self):
        self.newAccountPage = NewAccountPage(self.driver)
        self.newAccountPage.do_login(TestData.USER_ID, TestData.PASSWORD)

        self.newAccountPage.do_add_customer(TestData.CUSTOMER_DATA)

        (
            customer_id,
            customer_email,
            result_text,
        ) = self.newAccountPage.get_result_of_add_new_customer()

        # self.newAccountPage.do_add_new_account(customer_id, TestData.ACCOUNT_DATA)
        # text = self.newAccountPage.get_result_of_add_new_account()

        assert result_text == TestData.NEW_CUSTOMER_SUCCESS_TEXT
