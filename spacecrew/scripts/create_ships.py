#!/usr/bin/env python
# pyright: basic

import sys
from xmlrpc import client

root = 'http://localhost:8069'
db = 'vidi'
user = 'admin'
password = 'admin'

if __name__ == '__main__':
    common = client.ServerProxy(f'{root}/xmlrpc/2/common')
    print(common.version())

    uid = common.authenticate(db, user, password, {})
    print(f'{uid=}')

    models = client.ServerProxy(f'{root}/xmlrpc/2/object')
    model_access = models.execute_kw(db, uid, password,
                                     'spacecrew.spaceship', 'check_access_rights',
                                     ['write'], {'raise_exception': False})
    print(f'{model_access=}')

    res = models.execute_kw(db, uid, password,
                            'spacecrew.spaceship', 'create',
                            [[{'name': name} for name in sys.argv[1:]]])
    print(f'{res=}')
