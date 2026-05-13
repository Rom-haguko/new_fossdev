from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "discount-service"}


def test_student_promo_code_discount() -> None:
    response = client.post(
        "/discounts/calculate",
        json={
            "product_id": "pencil",
            "quantity": 2,
            "unit_price": 1.5,
            "promo_code": "STUDENT10",
        },
    )

    assert response.status_code == 200
    assert response.json()["discount_percent"] == 10.0


def test_bulk_discount() -> None:
    response = client.post(
        "/discounts/calculate",
        json={
            "product_id": "notebook",
            "quantity": 10,
            "unit_price": 4.2,
        },
    )

    assert response.status_code == 200
    assert response.json()["discount_percent"] == 7.0


def test_no_discount() -> None:
    response = client.post(
        "/discounts/calculate",
        json={
            "product_id": "pencil",
            "quantity": 1,
            "unit_price": 1.5,
        },
    )

    assert response.status_code == 200
    assert response.json()["discount_percent"] == 0.0
