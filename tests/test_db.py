from demowebsite.logic.db import get_db


def test_get_db():
    db = get_db()

    assert isinstance(db, dict)
    assert 'submissions' in db