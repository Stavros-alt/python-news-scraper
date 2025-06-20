import requests
from bs4 import BeautifulSoup

def scrape_hacker_news():
    """
    Scrapes headline titles and links from Hacker News homepage.
    Prints to console and saves to headlines.txt in format: "1. Headline Title (URL)"
    """
    try:
        # Send HTTP GET request to Hacker News
        print("Fetching Hacker News headlines...")
        response = requests.get("https://news.ycombinator.com")
        response.raise_for_status()  # Raise exception for bad status codes

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all headline links (current structure: inside <a> tags within <span class="titleline">)
        headlines = soup.select('span.titleline > a')
        
        # Prepare output
        console_output = []
        for idx, headline in enumerate(headlines, start=1):
            title = headline.text
            url = headline['href']
            console_output.append(f"{idx}. {title} ({url})")
        
        # Print to console
        print("\nTop Hacker News Headlines:")
        print("\n".join(console_output))
        
        # Save to file
        with open('headlines.txt', 'w', encoding='utf-8') as f:
            f.write("\n".join(console_output))
        print("\nHeadlines saved to headlines.txt")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Hacker News: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_hacker_news()