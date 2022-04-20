class TestData:

    LOGIN_URL = "https://demo.guru99.com/v4/"

    LOGIN_PAGE_TITLE = "Guru99 Bank Home Page"
    LOGOUT_PAGE_TITLE = "Guru99 Bank Home Page"
    NEW_CUSTOMER_PAGE_TITLE = "Guru99 Bank New Customer Entry Page"
    NEW_ACCOUNT_PAGE_TITLE = "Guru99 bank add new account"
    FUND_TRANS_PAGE_TITLE = "Guru99 Bank Fund Transfer Entry Page"
    WITHDRAW_PAGE_TITLE = "Guru99 Bank Amount Withdrawal Page"
    DEPOSIT_PAGE_TITLE = "Guru99 Bank Amount Deposit Page"
    CUS_STATEMENT_PAGE_TITLE = "Guru99 Bank Statement Page"

    LOGIN_PAGE_SUCCESS_TEXT = "Manger Id : mngr399425"
    LOGOUT_SUCCESS_TEXT = "You Have Succesfully Logged Out!!"
    NEW_CUSTOMER_SUCCESS_TEXT = "Customer Registered Successfully!!!"
    NEW_ACCOUNT_SUCCESS_TEXT = "Account Generated Successfully!!!"

    DEPOSIT_ACCOUNT_FAILURE_TEXT = "Account does not exist"
    WITHDRAW_ACCOUNT_FAILURE_TEXT = "Account does not exist"
    CUS_STATEMENT_FAILURE_TEXT = "Account does not exist"

    USER_ID = "mngr399425"
    PASSWORD = "jasyqEb"
	

    CUSTOMER_DATA = {
        "customer_name": "Pham Vo Hiep",
        "date_of_birth": "15081998",
        "address": "123",
        "city": "DN",
        "state": "Hoa Hai",
        "pin": "550000",
        "mobile_number": "123123123",
        "email": "phv@vku.udn.vn",
        "password": "123123123",
    }

    ACCOUNT_DATA = {
        "deposit": "100",
    }

    DEPOSIT_DATA = {
        "account_id": "46778",
        "amount": 200,
        "description": "test"
    }

    WITHDRAW_DATA = {
        "account_id": "46778",
        "amount": 200,
        "description": "test"
    }

    FUND_TRANS_DATA = {
        "account_payer_id": "46778",
        "account_payee_id": "46779",
        "amount": 200,
        "description": "test"
    }

    CUS_STATEMENT_DATA = {
        "account_id": "46779",
        "from_date": "01012022",
        "to_date": "01062022",
        "minimum_trans_value": 1000,
        "num_of_trans": 100
    }
