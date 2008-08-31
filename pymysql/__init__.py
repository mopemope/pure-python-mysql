VERSION = (0, 1, None)

def Connect(*args, **kwargs):
    from connections import Connection
    return Connection(*args, **kwargs)

connect = Connection = Connect

