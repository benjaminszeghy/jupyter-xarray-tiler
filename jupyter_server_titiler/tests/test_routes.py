import json


async def test_get_example(jp_fetch):
    response = await jp_fetch("jupyter-server-titiler", "get-example")

    assert response.code == 200
    payload = json.loads(response.body)
    assert payload == {
        "data": "This is /jupyter-server-titiler/get-example endpoint!"
    }
