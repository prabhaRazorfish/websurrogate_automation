import time

import requests


def get_first_response_OK(google_key):
    # The API endpoint
    url = f"https://2captcha.com/in.php?key=d89556512b156573f1b95540759f504b&method=userrecaptcha&googlekey={google_key}&pageurl=https://websurrogates01.azurewebsites.us/Home/AuthenticatePage"

    print("-------Final URL:--------------")
    print(url)
    # A GET request to the API
    response = requests.get(url)
    response_text = response.text
    print(response_text.split('|')[1])
    return response_text.split('|')[1]


def get_final_response_OK(google_key):
    response_key = get_first_response_OK(google_key)
    global response_text
    for i in range(10):
        url = f"https://2captcha.com/res.php?key=d89556512b156573f1b95540759f504b&action=get&id={response_key}"
        print(url)
        # A GET request to the API
        response = requests.get(url)
        print(response.text)
        if 'OK|' in response.text:
            print("Found!")
            response_text = response.text
            break
        time.sleep(6)

    print(response_text)
    return response_text.split('|')[1]


# def test_get_response_success(monkeypatch):
#     class MockResponse(object):
#         def __init__(self):
#             self.status_code = 200
#             self.url = "http://httpbin.org/get"
#             self.headers = {"foobar": "foooooo"}
#
#         def json(self):
#             return {"fooaccount": "foo123", "url": "https://fake-host.com"}
#
#     def mock_get(url):
#         return MockResponse()
#
#     monkeypatch.setattr(requests, "get", mock_get)
#     assert example2() == (200, "https://fake-host.com")