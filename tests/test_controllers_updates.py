from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from schemas.user import User
from schemas.account import Account
from schemas.card import Card

# Test parameters
test_name = 'Test User'
updated_name = 'test_user_update'
test_balance = 99999999999.99
test_payment = 5000.0
test_charge = 500.0
test_open_date = '2023-08-04 20:30:55.407318'
test_age = 10
test_cvv = '999'
expected_user_count = 1
expected_account_count = 1
expected_card_count = 1

def test_prerequisites():
    Card.delete().where(Card.cvv == test_cvv).execute()
    Account.delete().where(Account.open_date == test_open_date).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_user_update_name():
    test_user = UserController.create_user(age=test_age, name=test_name)

    update_test_user = UserController.update_name(test_user, updated_name)
    query_test_user = User.select().where(User.name == update_test_user.name) \
        .where(User.age == test_age)

    assert len(query_test_user) == expected_user_count

    User.delete().where(User.name ** f'%{updated_name}%').execute()

def test_account_update_payment():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    AccountController.update_balance_payment(test_account, test_payment)
    query_acct_balance = Account.select().where(Account.balance == (test_balance + test_payment))

    assert len(query_acct_balance) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_account_update_negative_payment_zero():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    AccountController.update_balance_payment(test_account, 0.0)
    query_acct_balance = Account.select().where(Account.balance == (test_balance + 0.0))

    assert len(query_acct_balance) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_account_update_negative_payment_under_zero():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    AccountController.update_balance_payment(test_account, -10.0)
    query_acct_balance = Account.select().where(Account.balance == (test_balance + 0.0))

    assert len(query_acct_balance) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_account_update_charge():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    AccountController.update_balance_charge(test_account, test_charge)
    query_acct_balance = Account.select().where(Account.balance == (test_balance - test_charge))

    assert len(query_acct_balance) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_account_update_charge_zero():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, 0.0, test_open_date)

    AccountController.update_balance_charge(test_account, test_charge)
    query_acct_balance = Account.select().where(Account.balance == (0.0))

    assert len(query_acct_balance) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_account_update_charge_under_zero():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    AccountController.update_balance_charge(test_account, (test_balance + test_charge))
    query_acct_balance = Account.select().where(Account.balance == test_balance)

    assert len(query_acct_balance) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()



def test_account_update_withdrawal():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    AccountController.update_balance_withdraw(test_account, test_charge)
    query_acct_balance = Account.select().where(Account.balance == (test_balance - test_charge))

    assert len(query_acct_balance) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_account_update_withdrawal_zero():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, 0.0, test_open_date)

    AccountController.update_balance_withdraw(test_account, test_charge)
    query_acct_balance = Account.select().where(Account.balance == (0.0))

    assert len(query_acct_balance) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_account_update_withdrawal_under_zero():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    AccountController.update_balance_withdraw(test_account, (test_balance + test_charge))
    query_acct_balance = Account.select().where(Account.balance == test_balance)

    assert len(query_acct_balance) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_card_update_name():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    test_card = CardController.create_card(test_account, test_user, test_cvv)
    CardController.update_name(test_card, 'Test User Update')

    query_card_name = Card.select().where(Card.name ** f'%{"Test User Update"}%')

    assert len(query_card_name) == expected_card_count

    Card.delete().where(Card.account_id == test_account).execute()
    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_card_update_cvv():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    test_card = CardController.create_card(test_account, test_user, test_cvv)
    CardController.update_cvv(test_card, '555')

    query_card_name = Card.select().where(Card.cvv == '555')

    assert len(query_card_name) == expected_card_count

    Card.delete().where(Card.account_id == test_account).execute()
    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_card_update_negative_cvv_4digits():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    test_card = CardController.create_card(test_account, test_user, test_cvv)
    CardController.update_cvv(test_card, '5555')

    query_card_name = Card.select().where(Card.cvv == test_cvv)

    assert len(query_card_name) == expected_card_count

    Card.delete().where(Card.account_id == test_account).execute()
    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()
