from math import radians, sin, cos, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2):
    R = 6371

    lat1, lon1, lat2, lon2 = map(
        radians, [lat1, lon1, lat2, lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def find_nearest(lat, lon, data):
    data = data.copy()

    data["distance_km"] = data.apply(
        lambda row: haversine(
            lat, lon, row["latitude"], row["longitude"]
        ),
        axis=1
    )

    return data.loc[data["distance_km"].idxmin()]


def get_prediction(water_level):
    depth = abs(float(water_level))

    if depth < 5:
        return {
            "suitability": "Highly Suitable",
            "color": "green"
        }

    elif depth < 15:
        return {
            "suitability": "Suitable",
            "color": "blue"
        }

    elif depth < 30:
        return {
            "suitability": "Moderately Suitable",
            "color": "orange"
        }

    else:
        return {
            "suitability": "Less Suitable / Critical Zone",
            "color": "red"
        }
