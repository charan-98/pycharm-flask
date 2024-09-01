import pytest
from main import app

@pytest.fixture()
def client():
    return app.test_client()

def test_page(client):
    res = client.get('/next')
    print(res)
    assert res.status_code == 200



