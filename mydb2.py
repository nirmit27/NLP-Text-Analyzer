""" DATABASE Management - CRUD Operations """

from mongo import Database


class DB:

    def __init__(self):
        self.db = Database()

    # Registration

    def add_creds(self, name, email, pwd):
        uniq_pwd = self.db.alt_find(field='creds.pwd', ch='n', value=pwd)
        uniq_email = self.db.alt_find(field='email', ch='n', value=email)

        if uniq_pwd and uniq_email:
            self.db.insert(name=name, email=email, pwd=pwd)
            return [1, uniq_pwd]

        return [0, uniq_pwd]

    # Login

    def search_creds(self, email, pwd):
        is_valid = self.db.alt_find(dic={"email": email, "creds.pwd": pwd})
        return True if is_valid else False


# ----------------------------------------------- D R I V E R ----------------------------------------------- #

if __name__ == "__main__":

    # Instantiating the DB class ...
    db = DB()

# ----------------------------------------------------------------------------------------------------------- #
