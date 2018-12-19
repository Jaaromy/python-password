from model.security import pwd_context as Context
from model.db import DB
import argparse

db = DB()


def startup():
    Context.load_path("./crypt.ini")
    parser = argparse.ArgumentParser(description="Securely process and store passwords")
    parser.add_argument("-u", "--user", help="User name", dest="user", required=True)
    parser.add_argument("-p", "--password", help="User's password", dest="password", required=True)
    parser.add_argument("-n", "--new", help="Create new user", dest="new", action="store_true")
    parser.add_argument("-a", "--admin", help="Is admin user", dest="admin", action="store_true")
    args = parser.parse_args()
    process(args)


def eval_hash_from_user(user, password):
    res = db.get_user(user)
    hsh = None

    if res:
        hsh = res["hash"]

    ok, new_hash = Context.verify_and_update(password, hsh)

    if ok and new_hash:
        db.update_hash(user, new_hash)

    return ok


def process(args):
    if args.new:
        db.create_user(args.user, args.password, args.admin)
        exit(0)

    valid = eval_hash_from_user(args.user, args.password)

    if valid:
        print("Login Success!")
    else:
        print("Login Failed!")


if __name__ == '__main__':
    startup()
