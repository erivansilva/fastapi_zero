from http import HTTPStatus

from fastapi.testclient import TestClient

from ..app import app


def test_root_deve_retornar_ola_mundo():
    cliente = TestClient(app)
    response = cliente.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo'}
    print(response)
