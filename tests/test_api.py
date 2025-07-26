from fastapi.testclient import TestClient

from rpn.main import app

client = TestClient(app)


def test_create_stack():
    response = client.post("api/stacks/")
    assert response.status_code == 200
    data = response.json()
    assert "stack_id" in data
    assert "stack" in data

    response = client.delete(f"api/stacks/{data['stack_id']}")
    assert response.status_code == 204


def test_push_token():
    response = client.post("api/stacks/")
    stack_id = response.json()["stack_id"]

    response = client.post(f"api/stacks/{stack_id}/push?token=5")
    assert response.status_code == 200
    assert response.json() == {"stack_id": stack_id, "stack": [5.0]}

    response = client.delete(f"api/stacks/{stack_id}")
    assert response.status_code == 204


def test_perform_subtract():
    response = client.post("api/stacks/")
    stack_id = response.json()["stack_id"]

    client.post(f"api/stacks/{stack_id}/push?token=5")
    client.post(f"api/stacks/{stack_id}/push?token=3")
    response = client.post(f"api/stacks/{stack_id}/push?token=%2D")

    assert response.status_code == 200
    assert response.json() == {"stack_id": stack_id, "stack": [2.0]}

    response = client.delete(f"api/stacks/{stack_id}")
    assert response.status_code == 204


def test_perform_multiply():
    response = client.post("api/stacks/")
    stack_id = response.json()["stack_id"]

    client.post(f"api/stacks/{stack_id}/push?token=5")
    client.post(f"api/stacks/{stack_id}/push?token=3")
    response = client.post(f"api/stacks/{stack_id}/push?token=%2A")

    assert response.status_code == 200
    assert response.json() == {"stack_id": stack_id, "stack": [15.0]}

    response = client.delete(f"api/stacks/{stack_id}")
    assert response.status_code == 204


def test_perform_divide():
    response = client.post("api/stacks/")
    stack_id = response.json()["stack_id"]

    client.post(f"api/stacks/{stack_id}/push?token=6")
    client.post(f"api/stacks/{stack_id}/push?token=3")
    response = client.post(f"api/stacks/{stack_id}/push?token=%2F")

    assert response.status_code == 200
    assert response.json() == {"stack_id": stack_id, "stack": [2.0]}

    response = client.delete(f"api/stacks/{stack_id}")
    assert response.status_code == 204


def test_divide_by_zero():
    response = client.post("api/stacks/")
    stack_id = response.json()["stack_id"]

    client.post(f"api/stacks/{stack_id}/push?token=6")
    client.post(f"api/stacks/{stack_id}/push?token=0")
    response = client.post(f"api/stacks/{stack_id}/push?token=/")

    assert response.status_code == 400
    assert "detail" in response.json()
    assert "Failed to push token: Cannot divide by zero." in response.json()["detail"]

    response = client.get(f"api/stacks/{stack_id}")
    assert response.status_code == 200
    assert response.json() == {"stack_id": stack_id, "stack": [6.0, 0.0]}

    response = client.delete(f"api/stacks/{stack_id}")
    assert response.status_code == 204


def test_get_unknown_stack():
    response = client.get("api/stacks/unknown_id")
    assert response.status_code == 404
    assert "detail" in response.json()
    assert "Stack with ID unknown_id does not exist." in response.json()["detail"]


def test_clear_stack():
    response = client.post("api/stacks/")
    stack_id = response.json()["stack_id"]

    client.post(f"api/stacks/{stack_id}/push?token=5")
    client.post(f"api/stacks/{stack_id}/push?token=3")

    response = client.post(f"api/stacks/{stack_id}/clear")
    assert response.status_code == 204

    response = client.get(f"api/stacks/{stack_id}")
    assert response.status_code == 200
    assert response.json() == {"stack_id": stack_id, "stack": []}

    response = client.delete(f"api/stacks/{stack_id}")
    assert response.status_code == 204


def test_clear_unknown_stack():
    # Attempt to clear an unknown stack
    response = client.post("api/stacks/unknown_id/clear")
    assert response.status_code == 404
    assert "detail" in response.json()
    assert "Stack with ID unknown_id does not exist." in response.json()["detail"]
