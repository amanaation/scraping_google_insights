# scraping_google_insights

## Installation
1. Download and Install Python 3.7.5
2. Download ChromeDriver 86.0.4240.22 from : ``` https://sites.google.com/a/chromium.org/chromedriver/downloads```
3. Clone the repository to your local repository.
4. Run the following command, to install required dependencies
  ```pip install -r requirements.txt```
5.Place the downloaded ChromeDriver as of the cloned github project folder

## Usage:

1. Open your command prompt and cd to your cloned directory.
2. Type following command in your cmd : 
    ``` python scraping_api.py ```
3. Open your browser and type the following url : 
    ```http://localhost:5000/post?from=20%20Jan%202020&to=20%20Mar%202020&duration=month&category=Toys```
    
## URL parameter details : 

1. from     : format =  DD MMM YYYY e.g. 20 Jan 2020
2. to       : format =  DD MMM YYYY e.g. 20 AUG 2020
3. duration : value = month/year
4. category : format = any string value e.g. Toys
