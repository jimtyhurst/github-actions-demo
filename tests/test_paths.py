from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_generic_greeting():
    response = client.get("/greeting")
    assert response.status_code == 200
    print(f"{response.json()=}")
    assert response.json() == {"message": "Hello, World!"}


def test_named_greeting():
    response = client.get("/greeting/Chris")
    assert response.status_code == 200
    print(f"{response.json()=}")
    assert response.json() == {"message": "Hello, Chris!"}


def test_named_greeting_with_arbitrary_string():
    expected_name = "3.14 * 2^3"
    response = client.get(f"/greeting/{expected_name}")
    assert response.status_code == 200
    print(f"{response.json()=}")
    assert response.json() == {"message": f"Hello, {expected_name}!"}
