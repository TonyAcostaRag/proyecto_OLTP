from schemas.account import Account
from schemas.user import User
from schemas.card import Card
from typing import Union


class CardController:

    # Create
    @staticmethod
    def create_card(account: Account, user: User, cvv: str) -> Card:
        card = Card(account_id=account.id, name=(user.name + ' debito ' + str(account.id)), cvv=cvv)
        card.save()
        return card

    # Read
    @staticmethod
    def get_card_by_id(id: int) -> Union[Card, None]:
        try:
            return Card.get(id=id)
        except Card.DoesNotExist:
            print("No matching card found.")
            return None

    @staticmethod
    def get_card_by_account(account: Account)-> Union[Card, None]:
        try:
            return Card.select().where(Card.account_id == account).get()
        except Card.DoesNotExist:
            return None

    # Update
    @staticmethod
    def update_name(card: Card, name: str):
        card.name = name + ' debito ' + str(card.account_id)
        card.save()
        return card

    @staticmethod
    def update_cvv(card: Card, cvv: str):
        if len(cvv) == 3:
            card.cvv = cvv
            card.save()
            return card

    # Delete
    @staticmethod
    def delete_card(card: Card):
        namecard = card.name
        account = Account.get(id=card.account_id)
        balance = account.balance
        if balance == 0:
            card.delete_instance()
            print(f'Card "{namecard}" is deleted.')
        else:
            print('Balance must be zero to delete this card')
