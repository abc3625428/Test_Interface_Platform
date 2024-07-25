

def md5_encrypt(data):

    import hashlib
    return hashlib.md5(data.encode('utf-8')).hexdigest()


