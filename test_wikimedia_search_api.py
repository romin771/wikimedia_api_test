import requests
import pytest

#  Our URL and query parameters
url = 'https://api.wikimedia.org/core/v1/wikipedia/en/search/page'
search_query = 'furry rabbits'
# the Sesame Street is not appearing on default limit with is 10, so adjust it to 20
number_of_results = 20
parameters = {'q': search_query, 'limit': number_of_results}


def test_earch_for_sesame_street():
    # Given: A client of the API
    # When: A search for pages containing 'furry rabbits' is executed
    response = requests.get(url, params=parameters)

    # Then: A page with the title 'Sesame Street' is found
    assert response.status_code == 200
    data = response.json()

    print("Response Data:")
    print(data)

    found_title = False
    for item in data.get('pages', []):
        if 'title' in item and item['title'] == 'Sesame Street':
            found_title = True
            break
    assert found_title, "Title 'Sesame Street' not found in the response."


if __name__ == '__main__':
    pytest.main(['test_wikimedia_api.py'])
