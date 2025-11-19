import requests

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "x-api-key": "reqres-free-v1"
}


def test_get_single_user():
    url = f"{BASE_URL}/users/2"
    response = requests.get(url, headers=HEADERS)

    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert "support" in data

    user = data["data"]

    assert "id" in user
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user
    assert "avatar" in user

    assert user["id"] == 2
    assert "@reqres.in" in user["email"]


def test_create_user_post():
    url = f"{BASE_URL}/users"
    payload = {
        "name": "Alexey",
        "job": "programmer"
    }

    response = requests.post(url, json=payload, headers=HEADERS)

    assert response.status_code == 201

    data = response.json()

    assert data.get("name") == payload["name"]
    assert data.get("job") == payload["job"]

    assert "id" in data
    assert "createdAt" in data


def test_update_user_put():
    url = f"{BASE_URL}/users/2"
    payload = {
        "name": "Dima",
        "job": "povar"
    }

    response = requests.put(url, json=payload, headers=HEADERS)

    assert response.status_code == 200

    data = response.json()

    assert data.get("name") == payload["name"]
    assert data.get("job") == payload["job"]

    assert "updatedAt" in data
