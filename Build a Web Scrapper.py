import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all article titles (modify the selector as per the website structure)
            # For example, if titles are in <h2> tags with class "entry-title":
            titles = soup.find_all('h2', class_='entry-title')

            # Extract and print the text from each title
            for title in titles:
                print(title.get_text(strip=True))
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
url = input("Enter the URL of the website to scrape titles from: ")
scrape_titles(url)
