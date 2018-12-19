from tinydb import TinyDB, Query
from model.security import pwd_context


class DB:
    def __init__(self):
        self.__db = TinyDB('./db/pass.json')
        self.__user_table = self.__db.table("user")
        self.__User = Query()

    def update_hash(self, user, new_hash):
        self.__user_table.upsert({"name": user, "hash": new_hash}, self.__User.name == user)
        print("Hash Updated")

    def create_user(self, user, password, admin):
        if admin:
            category = "admin"
        else:
            category = None

        n_hash = pwd_context.hash(password, category=category)
        self.update_hash(user, n_hash)
        print("User created successfully")

    def get_user(self, user):
        return self.__user_table.get(self.__User.name == user)
