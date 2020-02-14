"""
TEst the seldon deployment
"""


test_data = {"data":
     {"names":
        ["sepal_length", "sepal_width", "petal_length", "petal_width"],
      "ndarray": [[7.233, 4.652, 7.39, 0.324]]
     }
}

test_url = "http://localhost:5000/predict"


def test_predict():
    import requests
    res = requests.post(url=test_url, json=test_data)
    assert(res.ok)