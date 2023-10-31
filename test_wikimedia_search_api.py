import requests
import datetime


#  Our URL and query parameters
url = 'https://api.wikimedia.org/core/v1/wikipedia/en/search/page'
search_query = 'furry rabbits'
number_of_results = 20
parameters = {'q': search_query, 'limit': number_of_results}

#  Our  URL for getting page details 	/core/v1/{project}/{language}/page/{title}/bare
page_url = 'https://api.wikimedia.org/core/v1/wikipedia/en/page/'

# First Scenario
def test_earch_for_sesame_street():
    # Given: A client of the API
    # When: A search for pages containing 'furry rabbits' is executed
    response = requests.get(url, params=parameters)

    # Then: A page with the title 'Sesame Street' is found
    assert response.status_code == 200
    data = response.json()

    sesame_street_id = None
    for item in data.get('pages', []):
        if item.get('title') == 'Sesame Street':
            sesame_street_id = item.get('key')
            break
    assert sesame_street_id is not None,  "Sesame Street not found in search results."

    # Second Scenario
    # WHEN: The page information about  Sesame Street are requested
    page_response = requests.get(page_url + sesame_street_id + '/bare')
    assert page_response.status_code == 200
    page_data = page_response.json()

    # THEN: It has a latest timestamp > 2023-08-17
    timestamp_extract = page_data['latest']['timestamp']
    timestamp = datetime.datetime.strptime(timestamp_extract, '%Y-%m-%dT%H:%M:%SZ')
    our_date = datetime.datetime(2023, 8, 17)
    assert timestamp > our_date, "Latest timestamp is not greater than our provided date."