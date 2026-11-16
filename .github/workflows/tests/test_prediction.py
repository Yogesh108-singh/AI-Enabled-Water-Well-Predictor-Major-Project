import pandas as pd

from prediction_logic import (
    haversine,
    find_nearest,
    get_prediction
)


# Test 1: Check distance between same coordinates
def test_haversine():
    result = haversine(23.25, 77.41, 23.25, 77.41)
    assert result == 0


# Test 2: Check nearest water station
def test_find_nearest():
    data = pd.DataFrame({
        "latitude": [23.25, 24.00],
        "longitude": [77.41, 78.00]
    })

    result = find_nearest(23.25, 77.41, data)

    assert result["latitude"] == 23.25


# Test 3: Highly Suitable prediction
def test_highly_suitable():
    result = get_prediction(3)

    assert result["suitability"] == "Highly Suitable"
    assert result["color"] == "green"


# Test 4: Suitable prediction
def test_suitable():
    result = get_prediction(10)

    assert result["suitability"] == "Suitable"
    assert result["color"] == "blue"


# Test 5: Moderately Suitable prediction
def test_moderately_suitable():
    result = get_prediction(20)

    assert result["suitability"] == "Moderately Suitable"
    assert result["color"] == "orange"


# Test 6: Less Suitable prediction
def test_less_suitable():
    result = get_prediction(35)

    assert result["suitability"] == "Less Suitable / Critical Zone"
    assert result["color"] == "red"
