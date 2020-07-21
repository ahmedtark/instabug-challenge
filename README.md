# instabug-challenge
Third part: Test Automation
Search engine: WWW.GOOGLE.COM
  
------1st Testcase------- "No Results Found"
*Goal: Testing the search engine in searching for search term that has no results
*Test steps:
            1. Load home page for Google 
                                          ---> expected result: Google.com is loaded
            2. Enter random characters in the search box
            3. Press "Google Search" button 
                                          ---> expected result: the user is redirected to search results page
            4. verify that the loaded page corresponds to the desired search term
            5. verify that no results were found
            
------2nd Testcase------- "Results Found"       
*Goal: - Testing the search engine in searching for search term that has multiple search results
       - Testing the clear button in the searchbox functionality
       - Testing not entering a search term and pressing search button
*Test steps:
            1. Load home page for Google 
                                          ---> expected result: Google.com is loaded
            2. Enter a search term in the search box
            3. Press the clear button in the searchbox
                                          ---> expected result: search box is empty
            4. Press "Google Search" button 
                                          ---> expected result: the user is still on the google.com homepage
            5. Enter intended search term in the search box and press "Google Search" button 
                                          ---> expected result: the user is redirected to search results page
            6. Verify that the loaded page corresponds to the desired search term
            7. Check the number of found results
