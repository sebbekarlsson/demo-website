from demowebsite.logic.submit import submit_submission
from demowebsite.logic.db import get_db
from demowebsite.models.submission import Submission


def test_submit_submission():
    db = get_db()
    length_before = len(db['submissions'])

    submission = Submission(title="hej hej", description="yoyo")
    submit_submission(submission)

    sub = None

    for submission in db['submissions']:
        if submission['title'] == 'hej hej':
            sub = submission
            break

    assert sub is not None
