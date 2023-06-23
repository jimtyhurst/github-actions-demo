from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def build_expected_greeting(expected_name="World") -> str:
    return f"Hello, {expected_name}!"


def test_generic_greeting():
    expected_name = "World"
    response = client.get("/greeting")
    assert response.status_code == 200
    print(f"{response.json()=}")
    assert response.json() == {"message": build_expected_greeting(expected_name)}


def test_named_greeting():
    expected_name = "Chris"
    response = client.get(f"/greeting/{expected_name}")
    assert response.status_code == 200
    print(f"{response.json()=}")
    assert response.json() == {"message": build_expected_greeting(expected_name)}


def test_named_greeting_with_arbitrary_string():
    expected_name = "3.14 * 2^3"
    response = client.get(f"/greeting/{expected_name}")
    assert response.status_code == 200
    print(f"{response.json()=}")
    assert response.json() == {"message": build_expected_greeting(expected_name)}
