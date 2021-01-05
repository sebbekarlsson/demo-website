from demowebsite.logic.db import get_db, save_db


def submit_submission(submission):
    db = get_db()
    submission.idx = len(db['submissions']) + 1
    db['submissions'].append(submission.__dict__)
    save_db(db)

    return submission


def get_submission_by_id(idx):
    db = get_db()
    submissions = db['submissions']

    print(submissions)

    for submission in submissions:
        if str(submission['idx']) == str(idx):
            return submission