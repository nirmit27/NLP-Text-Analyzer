""" Database Management """

import json


class Database:

    def __init__(self):
        pass

    # Registration
    def add_data(self, name, email, pwd):

        uniq_pwd = True

        with open('db.json', 'r') as rf:
            database = json.load(rf)

        for i in database.items():
            if pwd == i[1][1]:
                uniq_pwd = False

        if email not in database and uniq_pwd:
            database[email] = [name, pwd]
            with open('db.json', 'w') as wf:
                json.dump(database, wf)
            return [1, uniq_pwd]
        return [0, uniq_pwd]

    # Login
    def search(self, email, pwd):
        with open('db.json', 'r') as rf:
            database = json.load(rf)
            if email in database.keys():
                if pwd in database[email][1]:
                    return 1
                else:
                    return 0
            else:
                return 0


if __name__ == "__main__":
    sample = Database()
    sample.add_data('', '', '')
