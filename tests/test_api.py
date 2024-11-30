import pytest
import requests
BASE_URL = "http://localhost:5000/"

def test_get_endpoint():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert response.json() == {"message": "¡Hola desde Flask!"}

def test_saludo_endpoint():
    response = requests.get(BASE_URL + "saludo/World")
    assert response.status_code == 200
    assert response.json() == {"message": "¡Hola World!"}

def test_about_endpoint():
    response = requests.get(BASE_URL + "about")
    assert response.status_code == 200
    assert response.json() == {"message": "About Us"}