from schemas.account import Account
from schemas.user import User
from schemas.card import Card
from typing import Union

from datetime import datetime


class AccountController:

    # Create account
    @staticmethod
    def create_account(
            user: User,
            balance: float,
            open_date: datetime) -> Account:
        account = Account(
            user_id=user.id,
            balance=balance,
            open_date=open_date)
        account.save()
        return account

    # Read
    @staticmethod
    def get_account_by_id(id: int) -> Account:
        #return Account.get(id=id)
        try:
            return Account.select().where(Account.id == id).get()
        except Account.DoesNotExist:
            return None

    @staticmethod
    def get_account_by_user(user: User) -> Union[Account, None]:
        try:
            return Account.get(user_id=user.id)
        except Account.DoesNotExist:
            print("No matching user found.")
            return None

    @staticmethod
    def get_account_by_card(card: Card) -> Account:
        #return Card.get(id=card)
        try:
            return Card.select().where(Card.id == card).get()
        except:
            return None

    # Update
    @staticmethod
    def update_balance_payment(account: Account, amount: float) -> Account:
        if (amount > 0):
            account.balance += amount
            account.save()
        return Account.select().where(Account.id == account.user_id).get()

    @staticmethod
    def update_balance_charge(account: Account, amount: float) -> Account:
        if (account.balance > 0 and amount <= account.balance):
            account.balance -= amount
            account.save()
        return Account.select().where(Account.id == account.user_id).get()

    @staticmethod
    def update_balance_withdraw(account: Account, amount: float) -> Account:
        if (account.balance > 0 and amount <= account.balance):
            account.balance -= amount
            account.save()
        return Account.select().where(Account.id == account.user_id).get()

    # Delete
    @staticmethod
    def delete_account(account: Account):
        accountid = account.id
        try:
            card = Account.get(account_id=account.id)
        except:
            print("No matching account found.")
            card = None
        if card is None:
            account.delete_instance()
            print(f'Account "{accountid}" is deleted!')
        else:
            card.delete_instance()
            account.delete_instance()
