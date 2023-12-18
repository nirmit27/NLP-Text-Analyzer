""" MongoDB Connectivity """

import configparser as cfgp
from pymongo import MongoClient


def listAll(client):
    dbs = client.list_database_names()

    print("Available databases :\n")
    for db in dbs:
        print(db, end='\t')


def insertion(client):

    pass


if __name__ == "__main__":

    # Fetching the connection string from the CONFIG file ...
    cfg = cfgp.ConfigParser()
    cfg.read('settings.cfg')
    connectionString = cfg.get('MDB', 'connectionString')

    # Establishing the connection ...
    client = MongoClient(connectionString)

    # insertion(client)
    listAll(client)

    # Closing the connection ...
    client.close()
