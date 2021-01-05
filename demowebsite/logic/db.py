import json
import os


DB_FILE = 'db.json'

def get_db():
    if not os.path.isfile(DB_FILE):
        return {"submissions": []}

    return json.loads(open(DB_FILE).read())


def save_db(db):
    return open(DB_FILE, 'w+').write(json.dumps(db))