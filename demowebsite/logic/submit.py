from demowebsite.logic.db import get_db, save_db


def submit_submission(submission):
    db = get_db()
    db['submissions'].append(submission.__dict__)
    save_db(db)