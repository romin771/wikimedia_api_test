# Wikimedia Search API Test

This repository contains a simple Python test for testing the Wikimedia Search API. It covers two different scenarios as : 
Scenario 1:
- GIVEN
o A client of the API
- WHEN
o A search for pages containing for ‘furry rabbits’ is executed
- THEN
o A page with the title ‘Sesame Street’ is found


Scenario 2:
- GIVEN
o The result for ‘furry rabbits’ search contains ‘Sesame Street’
- WHEN
o The page details for Sesame Street are requested
- THEN
o It has a latest timestamp > 2023-08-17




## Running the Test

To run this test, you'll need to have Python, pytest, and the following Python packages installed on your machine : 

- json
- requests
- datetime

1. **Install Packages**

   If you don't have Python installed, download and install it from : [python.org](https://www.python.org/downloads/).

   and for installing the rest of the packages, follow the steps:

   ```bash
   pip install pytest
   pip install json
   pip install requests
   pip install datetime

2. **Clone this Repository**
     Clone this repository to your local machine with git clone or download it as a ZIP file.

4. **Run the Test**
   Navigate to the directory where this test (test_wikimedia_search_api.py) is located. Open a terminal or command prompt, and run the test using pytest:

   ```bash
   pytest test_wikimedia_search_api.py
  

