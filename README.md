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

1. **Clone this Repository**
     Clone this repository to your local machine with git clone or download it as a ZIP file, extract it.

2. **Install Packages**
   If you don't have Python installed, download and install it from : [python.org](https://www.python.org/downloads/).
     You also need to have Pip install on your machine in order to be able to install the other packages. You can install pip from : ([https://pip.pypa.io/en/stable/installation/](https://packaging.python.org/en/latest/tutorials/installing-packages/))

   and for installing the rest of the packages, navigate to the directory where this test (test_wikimedia_search_api.py) is located. Open a terminal or command prompt, Or open the project and inside the terminal of your IDE follow the steps:

   ```bash
   pip install pytest
   pip install json
   pip install requests
   pip install datetime


4. **Run the Test**
   While you are in the test directory or you have IDE terminal open,  run the test using pytest:

   ```bash
   pytest test_wikimedia_search_api.py

## Other TestCase/Scenarios To Consider

   1 - Test Case: Verify image URLs in Search Results: 

   Scenario Title: Check All Search Results with Thumbnails Have Valid URLs
   Explanation: This test checks that every search result with a thumbnail has a valid URL. It checks that the 'thumbnail' key exists and that the 'url' in each thumbnail is a valid URL. It's important  that images can be loaded and displayed correctly.

   2 - Test Case : Validate Image Dimensions in Search Results
   
   Scenario Title: Make sure Thumbnails Have Expected Height and Width in Search Results
   Explanation: This test checks that the height and width of thumbnail images in search results match the expected values. It checks that each thumbnail's 'height' and 'width' match the predefined values.

And many other scenarios such as : Verify License Information for 'Sesame Street' Page  and etc 

   


  

