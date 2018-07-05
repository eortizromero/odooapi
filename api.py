# -*- coding: utf-8 -*-

import erppeek


def get_database(host, port=None, pwd=None):
    client = erppeek.Client(server=host)
    db = client.db.list()
    return db
