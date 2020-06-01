import requests

def test_stCode():
    post_data= {
        "full_name": "Idris Shabanli"
    }
    response = requests.post('http://35.225.243.133/bloggers/',data=post_data)
    expected_status_code = 201
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code
    expected_name = post_data["full_name"]
    actual_name = response.json()["full_name"]
    assert expected_name == actual_name


def test_invalid_data():
    post_data = {
        "full_name": "abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd abcd"
    }
    response = requests.post('http://35.225.243.133/bloggers/', data=post_data)
    expected_status_code = 400
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code
    expected_name = ["Ensure this field has no more than 180 characters."]
    actual_name = response.json()["full_name"]
    assert expected_name == actual_name

def test_invalid_data2():
    post_data = {}
    response = requests.post('http://35.225.243.133/bloggers/', data=post_data)
    expected_status_code = 400
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code
    expected_name = ["This field is required."]
    actual_name = response.json()["full_name"]
    assert expected_name == actual_name

def test_invalid_data3():
    post_data = {
        "id": 1223
    }
    response = requests.post('http://35.225.243.133/bloggers/', data=post_data)
    expected_status_code = 400
    actual_status_code = response.status_code
    assert expected_status_code == actual_status_code
    expected_name = ["This field is required."]
    actual_name = response.json()["full_name"]
    assert expected_name == actual_name