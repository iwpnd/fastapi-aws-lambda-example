from starlette.testclient import TestClient
from example_app.main import app
from example_app.core.config import API_V1_STR
import json

client = TestClient(app)


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True


def test_example_endpoint_availability():
    response = client.get(API_V1_STR + "/example")
    assert response.status_code == 200


def test_example_route_valid_json():
    response = client.get(API_V1_STR + "/example")
    assert is_json(response.content)


def test_example_endpoint_post():
    payload = {"a": 4, "b": 6}
    response = client.post(API_V1_STR + "/example", json=payload)
    assert response.status_code == 200
    assert all([k in response.json() for k in ["a", "b", "result"]])
    assert response.json()["result"] == 24
