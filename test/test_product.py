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


def test_list_product(client):
    p1 = product.create(name="product1", price=10000)
    p2 = product.create(name="product2", price=10000)
    p3 = product.create(name="product3", price=10000)

    response = client.get("/product?page=1&per_page=2")

    expected = {
        "has_prev": False,
        "has_next": True,
        "products": [{
            "id": p1.id,
            "name": "product1",
            "price": 10000
        }, {
            "id": p2.id,
            "name": "product2",
            "price": 10000
        }]
    }
    assert response.json == expected

    response2 = client.get("/product?page=2&per_page=2")

    expected2 = {
        "has_prev": True,
        "has_next": False,
        "products": [{
            "id": p3.id,
            "name": "product3",
            "price": 10000
        }]
    }
    assert response2.json == expected2
