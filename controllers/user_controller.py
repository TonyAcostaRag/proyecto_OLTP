from schemas.user import User
from schemas.account import Account
from controllers.account_controller import AccountController


class UserController:

    # Create
    @staticmethod
    def create_user(age: int, name: str) -> User:
        user = User(age=age, name=name)
        user.save()
        return user

    # Read
    @staticmethod
    def get_user_by_id(id: int) -> User:
        try:
            return User.select().where(User.id == id).get()
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user_by_name(name: str) -> User:
        try:
            return User.select().where(User.name == name).get()
        except User.DoesNotExist:
            return None

    # Update
    @staticmethod
    def update_name(user: User, name: str) -> User:
        user.name = name
        user.save()
        return user

    # Delete
    @staticmethod
    def delete_user(user: User):
        username = user.name
        try:
            account = Account.get(user_id=user.id)
        except:
            account = None
        if account is None:
            user.delete_instance()
            print(f'User "{username}" is deleted!')
        else:
            AccountController.delete_account(account=account)
            user.delete_instance()
