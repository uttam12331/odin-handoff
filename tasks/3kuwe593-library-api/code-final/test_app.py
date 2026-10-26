import app as api

GOOD = {'title': 'Test Book', 'author': 'Ana Reyes', 'isbn': '9780306406157', 'published_year': 2020, 'pages': 320}

def test_rules(tmp_path, monkeypatch):
    monkeypatch.setattr(api, 'DB', str(tmp_path / 'test.db'))
    api.init_db()
    c = api.app.test_client()
    assert c.post('/books', json=GOOD).status_code == 201
    assert c.post('/books', json=GOOD).status_code == 409
    for bad in [{'title': ''}, {'isbn': '9780306406158'}, {'published_year': 3000}, {'pages': 0}]:
        assert c.post('/books', json={**GOOD, **bad}).status_code == 400
