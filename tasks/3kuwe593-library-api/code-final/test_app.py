import app as api

GOOD = {'title': 'Test', 'author': 'Ana', 'isbn': '9780306406157', 'published_year': 2020, 'pages': 320}

def test_rules(tmp_path, monkeypatch):
    monkeypatch.setattr(api, 'DB', str(tmp_path / 'test.db'))
    api.init_db()
    c = api.app.test_client()
    for change, code in [({}, 201), ({}, 409), ({'title': ''}, 400), ({'isbn': '9780306406158'}, 400), ({'published_year': 3000}, 400), ({'pages': 0}, 400)]:
        assert c.post('/books', json={**GOOD, **change}).status_code == code
