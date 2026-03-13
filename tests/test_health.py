from health_app.health import get_ideal_weight, get_health_advice

def test_ideal_weight():
    assert get_ideal_weight(1.5) == 49.5

def test_get_health_advice():
    assert get_health_advice({"bmi_category": "Underweight"}) == "Eat until you are full every meal, dont skip any meals, include saturated fats and protein"
    assert get_health_advice({"bmi_category": "x"}) == "x is not a valid category"