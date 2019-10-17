from app import product


def test_create(client):
    response = client.post("/product", data={
        "name": "sepatu",
        "price": 10000
    })

    expected = {
        "id": 1,
        "name": "sepatu",
        "price": 10000
    }

    assert response.json == expected


def test_read(client):
    p = product.create(name="sepatu", price=10000)
    response = client.get(f"/product/{p.id}")

    expected = {
        "id": p.id,
        "name": "sepatu",
        "price": 10000
    }

    assert response.json == expected


def test_delete(client):
    p = product.create(name="sepatu", price=10000)
    response = client.delete(f"/product/{p.id}")

    expected = {
        "message": "delete success"
    }

    assert response.json == expected


def test_update(client):
    p = product.create(name="sepatu", price=10000)
    response = client.post(f"/product/{p.id}", data={
        "name": "baju",
        "price": 50000
    })

    expected = {
        "id": p.id,
        "name": "baju",
        "price": 50000
    }

    assert response.json == expected
