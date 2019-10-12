def test_create(client):
    response = client.post("/user", data={
        "username": "faisal",
        "email": "faisalburhanudin@gmail.com"
    })

    expected = {
        "id": 1,
        "username": "faisal",
        "email": "faisalburhanudin@gmail.com",
        "photo": "",
        "clothes_size": None
    }

    assert response.json == expected
