from db.migrations import create_db
from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController

from schemas.user import User
from schemas.account import Account
from schemas.card import Card

from datetime import datetime


if __name__ == '__main__':
    create_db('db/db_oltp.db')

    print('\nInitial deletions:')
    print(f'\nUser deleted records: {User.delete().execute()}')
    print(f'Account deleted records: {Account.delete().execute()}')
    print(f'Card deleted records: {Card.delete().execute()}')

    current_datetime = datetime.now()

    # Create

    user_1 = UserController.create_user(age=29, name='Tony')

    account_1 = AccountController.create_account(user=user_1,
                                                 balance=0.0,
                                                 open_date=current_datetime)

    card_1 = CardController.create_card(account=account_1, user=user_1, cvv='111')

    # User_1 data
    print('\n\nCreations:')
    print(f"\nUser_1 data:"
                    f"\n\tuser 1 id: {user_1.id},"
                    f"\n\tuser 1 age: {user_1.age},"
                    f" \n\tuser 1 name: {user_1.name}")

    # Account_1 data
    print(f"\nAccount_1 data:"
                    f"\n\taccount 1 id: {account_1.id},"
                    f"\n\taccount 1 user_id: {account_1.user_id},"
                    f"\n\taccount 1 balance: {account_1.balance},"
                    f"\n\taccount 1 open_date: {account_1.open_date}")

    # Card_1 data
    print(f"\nCard_1 data:"
                    f"\n\tcard 1 id: {card_1.id},"
                    f"\n\tcard 1 account_id: {card_1.account_id},"
                    f"\n\tcard 1 name: {card_1.name},"
                    f"\n\tcard 1 cvv: {card_1.cvv}")

    # Retrieve
    print('\n\nRetrievals:')
    # User retrieving by id
    print(f"\nRetrieving user by id: {UserController.get_user_by_id(1)}")
    user_by_id = UserController.get_user_by_id(1)
    query_user_by_id = User.select().where(User.id == user_by_id)
    for i in query_user_by_id:
        print(i.id, i.age, i.name)


    # User retrieving by name
    print(f"\nRetrieving user by name: {UserController.get_user_by_name('Tony')}")
    user_by_name = UserController.get_user_by_name('Tony')
    query_user_by_name = User.select().where(User.id == user_by_name)
    for i in query_user_by_name:
        print(i.id, i.age, i.name)

    # Account retrieving by id
    print(f"\nRetrieving account by id: {AccountController.get_account_by_id(1)}")
    account_by_id = AccountController.get_account_by_id(1)
    query_account_by_id = Account.select().where(Account.id == account_by_id)
    for i in query_account_by_id:
        print(i.id, i.user_id, i.balance, i.open_date)

    # Account retrieving by user
    print(f"\nRetrieving account by user: {AccountController.get_account_by_user(user_1)}")
    account_by_user = AccountController.get_account_by_user(user_1)
    query_account_by_user = Account.select().where(Account.id == account_by_user)
    for i in query_account_by_user:
        print(i.id, i.user_id, i.balance, i.open_date)

    # Account retrieving by card
    print(f"\nRetrieving account by card: {AccountController.get_account_by_card(card_1)}")
    account_by_card = AccountController.get_account_by_card(card_1)
    query_account_by_card = Account.select().where(Account.id == account_by_card)
    for i in query_account_by_card:
        print(i.id, i.user_id, i.balance, i.open_date)

    # Card retrieving by id
    print(f"\nRetrieving card by id: {CardController.get_card_by_id(1)}")
    card_by_id = CardController.get_card_by_id(1)
    query_card_by_id = Card.select().where(Card.id == card_by_id)
    for i in query_card_by_id:
        print(i.id, i.account_id, i.name, i.cvv)

    # Card retrieving by account
    print(f"\nRetrieving card by account: {CardController.get_card_by_account(account_1)}")
    card_by_account = CardController.get_card_by_account(account_1)
    query_card_by_account = Card.select().where(Card.id == card_by_account)
    for i in query_card_by_account:
        print(i.id, i.account_id, i.name, i.cvv)


    # Updations
    print('\n\nUpdations:')

    # User update name
    print(f'\nUser update name: {user_1.name}')
    updated_user_name = UserController.update_name(user_1, 'Antonio')
    query_user_by_name = User.select().where(User.id == updated_user_name)
    for i in query_user_by_name:
        print(i.id, i.age, i.name)

    # Account update balance due payment
    print(f'\nAccount update balance due payment. Current balance: {account_1.balance}')
    updated_account_balance_payment = AccountController.update_balance_payment(account_1, 5000.0)
    query_acct_balance = Account.select().where(Account.id == updated_account_balance_payment)
    for i in query_acct_balance:
        print(i.id, i.user_id, i.balance, i.open_date)

    # Account update balance due charge
    print(f'\nAccount update balance due charge. Current balance: {account_1.balance}')
    updated_account_balance_charge = AccountController.update_balance_charge(account_1, 500.0)
    query_acct_balance = Account.select().where(Account.id == updated_account_balance_charge)
    for i in query_acct_balance:
        print(i.id, i.user_id, i.balance, i.open_date)

    # Account update balance due withdrawal
    print(f'\nAccount update balance due withdrawal. Current balance: {account_1.balance}')
    updated_account_balance_withdrawal = AccountController.update_balance_withdraw(account_1, 1000.0)
    query_acct_balance = Account.select().where(Account.id == updated_account_balance_withdrawal)
    for i in query_acct_balance:
        print(i.id, i.user_id, i.balance, i.open_date)

    # Card update name
    print(f'\nCard update name. Current name: {card_1.name}')
    updated_card_name = CardController.update_name(card_1, 'Antonio')
    query_card_name = Card.select().where(Card.id == updated_card_name)
    for i in query_card_name:
        print(i.id, i.account_id, i.name, i.cvv)

    # Card update cvv
    print(f'\nCard update cvv. Current cvv: {card_1.cvv}')
    updated_card_cvv = CardController.update_cvv(card_1, '222')
    query_card_cvv = Card.select().where(Card.id == updated_card_cvv)
    for i in query_card_cvv:
        print(i.id, i.account_id, i.name, i.cvv)


    # Deletions
    print('\n\nDeletions')

    # Card deletion
    print(f'\nDeletion of card: {card_1.name}')
    AccountController.update_balance_withdraw(account_1, 3500.0)
    CardController.delete_card(card_1)

    # Account deletion
    print(f'\nDeletion of account: {account_1.user_id}')
    AccountController.delete_account(account_1)

    # User deletion
    print(f'\nDeletion of user: {user_1.name}')
    UserController.delete_user(user_1)


    print('\n\nShowing all records in 3 tables:')

    print("\nUser records: ")
    for i in User.select():
        print(i.id, i.age, i.name)

    print("\nAccount records: ")
    for i in Account.select():
        print(i.id, i.user_id, i.balance, i.open_date)

    print("\nCard records: ")
    for i in Card.select():
        print(i.id, i.account_id, i.name, i.cvv)

