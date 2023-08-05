from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from schemas.user import User
from schemas.account import Account
from schemas.card import Card

# Test parameters
test_name = 'Test User'
test_balance = 99999999999.99
test_open_date = '2023-08-04 20:30:55.407318'
test_age = 10
test_cvv = '999'
expected_user_count = 1
expected_account_count = 1
expected_card_count = 1

def test_prerequisites():
    Card.delete().where(Card.cvv == test_cvv).execute()
    Account.delete().where(Account.balance == test_balance).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_user_creation():

    test_user = UserController.create_user(age=test_age, name=test_name)
    query_test_user = User.select().where(User.name == test_name)\
                                    .where(User.age == test_age)

    assert test_user is not None
    assert isinstance(test_user, User)
    assert len(query_test_user) == expected_user_count

    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_account_creation():
    test_user = UserController.create_user(age=test_age, name=test_name)

    test_account = AccountController.create_account(test_user, test_balance, test_open_date)
    query_test_account = Account.select().where(Account.user_id == test_user.id)\
                                        .where(Account.balance == test_balance)\
                                        .where(Account.open_date == test_open_date)

    assert test_account is not None
    assert isinstance(test_account, Account)
    assert len(query_test_account) == expected_account_count

    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()

def test_card_creation():
    test_user = UserController.create_user(age=test_age, name=test_name)
    test_account = AccountController.create_account(test_user, test_balance, test_open_date)

    test_card = CardController.create_card(test_account, test_user, test_cvv)
    query_test_card = Card.select().where(Card.account_id == test_account.id)\
                                    .where(Card.name ** f'%{test_name}%')\
                                    .where(Card.cvv == test_cvv)

    assert test_card is not None
    assert isinstance(test_card, Card)
    assert len(query_test_card) == expected_card_count

    Card.delete().where(Card.account_id == test_account).execute()
    Account.delete().where(Account.user_id == test_user).execute()
    User.delete().where(User.name ** f'%{test_name}%').execute()
