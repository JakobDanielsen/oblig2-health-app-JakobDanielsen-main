from health_app.data import jsonObject

def test_json_object_structure():
    data = jsonObject()
    for entry in data:
        assert "name" in entry
        assert "weight_kg" in entry
        assert "height_m" in entry