""" MongoDB Connectivity """

from pprint import pprint
import configparser as cfgp
from pymongo import MongoClient


class Database:

    # Establishing connection ...

    def __init__(self):
        cfg = cfgp.ConfigParser()
        cfg.read('config/connectsettings.cfg')
        connectionString = cfg.get('MDB', 'connectionString')
        self.client = MongoClient(connectionString)
        self.available_dbs = self.client.list_database_names()

    # Fetching the desired db/collection reference ...

    def fetch(self, db_name='', collection_name=''):
        if db_name == '' and collection_name == '':
            db_name = input("\nEnter the database name : ")
            collection_name = input("\nEnter the collection name : ")
        try:
            if db_name not in self.available_dbs:
                raise ValueError(f"\nDatabase {db_name} not found!\n")
            if collection_name not in self.client[db_name].list_collection_names():
                raise ValueError(
                    f"\nCollection {collection_name} doesn't exist!\n")
            return self.client[db_name][collection_name]
        except ValueError as e:
            print(e)

    # Showing all the  A V A I L A B L E  dbs ...

    def show_dbs(self):
        print("\nAvailable databases in the cluster :", end='   ')
        for i in range(len(self.available_dbs)):
            if i == (len(self.available_dbs) - 1):
                print(self.available_dbs[i], end='')
            else:
                print(self.available_dbs[i], end=', ')
        print()

    # Viewing all the  C O L L E C T I O N S  in the dbs ...

    def view_collections(self, db_name):
        collections = self.client[db_name].list_collection_names()
        print(
            f"\nAvailable collections in the {db_name} database :", end='   ')
        for i in range(len(collections)):
            if i == (len(collections) - 1):
                print(collections[i], end='')
            else:
                print(collections[i], end=', ')
        print()

    # Updating the database ...

    def insert(self, n=1, name='', email='', pwd=''):
        collection = self.fetch('nlpApp', 'creds')
        if collection != None:
            if n < 0:
                print(f"\nNumber of documents must be >= 1\n")
                return
            else:
                if n == 1:
                    if name == '' and email == '' and pwd == '':
                        name = input("\nEnter user's name: ")
                        email = input("\nEnter user's email id: ")
                        pwd = input("\nEnter user's password: ")
                    new_user = {
                        "email": email,
                        "creds": {
                            "name": name,
                            "pwd": pwd
                        }
                    }
                    id = collection.insert_one(new_user)
                elif n > 1:
                    docs = []
                    n = int(
                        input("\nEnter the number of documents to be inserted : "))
                    for i in range(n):
                        print(f"\nEnter the credentials of user #{i+1} ...")
                        name = input("\nEnter user's name: ")
                        email = input("\nEnter user's email id: ")
                        pwd = input("\nEnter user's password: ")
                        docs.append({
                            "email": email,
                            "creds": {
                                "name": name,
                                "pwd": pwd
                            }
                        })
        else:
            print("\nInsertion operation F A I L E D.\n")

    # Querying the database ...

    def find(self):
        collection = self.fetch()
        if collection != None:
            result = {}
            field = input("\nEnter the query field : ")
            ch = input("\nIs the value numeric? (y/n)  >>  ")
            value = int(input("\nEnter the query value : ")
                        ) if ch == 'y' else input("\nEnter the query value : ")
            doc_to_find = {field: value}
            result = collection.find_one(doc_to_find)
            if result != None:
                print("\nQuery ran successfully! Result ...\n")
                pprint(result)
            else:
                print("\nNo such documents exist!\n")
        else:
            print("\nFailed Query operation!\n")

    def alt_find(self, field='', ch='', value='', dic={}):
        collection = self.fetch(db_name='nlpApp', collection_name='creds')
        if collection != None:
            doc_to_find, result = {}, {}
            if field == '' and ch == '' and value == '' and len(dic) == 0:
                field = input("\nEnter the query field : ")
                ch = input("\nIs the value numeric? (y/n)  >>  ")
                value = int(input("\nEnter the query value : ")
                            ) if ch == 'y' else input("\nEnter the query value : ")
                doc_to_find = {field: value}
                result = collection.find_one(doc_to_find)
            elif len(dic) != 0:
                result = collection.find_one(dic)
            if result != None:
                return True
            else:
                return False
        else:
            return False

    # for MULTIPLE conditional matches ...

    def conditional_find(self):
        collection = self.fetch()
        if collection != None:
            field = input("\nEnter the query field : ")
            ch = input("\nIs the value numeric? (y/n)  >>  ")
            value = int(input("\nEnter the query value : ")
                        ) if ch == 'y' else input("\nEnter the query value : ")
            condition = input("\nEnter the conditional query operator : ")
            doc_to_find = {field: {f"${condition}": value}}
            cursor = collection.find(doc_to_find)
            if cursor != None:
                n = 0
                print("\nQuery ran successfully! Results ...\n")
                for doc in cursor:
                    n += 1
                    pprint(doc)
                    print()
                print(f"\nNumber of matches = {n}")
            else:
                print("\nNo such documents exist!\n")
        else:
            print("\nFailed Query operation!\n")

    # Closing the connection ...

    def close_connection(self):
        print(f"\n{'C L O S I N G  C O N N E C T I O N'.center(50, ' ')}\n")
        self.client.close()


# ----------------------------------------------- D R I V E R ----------------------------------------------- #

if __name__ == "__main__":

    database = Database()

    # Checking if everything is OK ...
    database.show_dbs()

    #  C R U D  Operations ...

    # database.find()
    # database.insert(n=1)
    # database.conditional_find()

    database.close_connection()

# ----------------------------------------------------------------------------------------------------------- #
