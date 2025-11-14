import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_channel_videos(channel_url):
    """
    Scrapes video links, titles, and published dates from a YouTube channel.
    Args:
        channel_url (str): URL of the YouTube channel.
    Returns:
        list: A list of dictionaries containing video information.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    
    # Add "/videos" to ensure we scrape the video tab
    videos_url = channel_url.rstrip("/") + "/videos"
    response = requests.get(videos_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch channel page. HTTP Status Code: {response.status_code}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract video information
    videos_data = []
    video_elements = soup.find_all("a", id="video-title")
    
    for video in video_elements:
        video_title = video["title"]
        video_link = "https://www.youtube.com" + video["href"]
        published_date = video.find_next("span", class_="style-scope ytd-grid-video-renderer").text.strip()
        
        videos_data.append({
            "title": video_title,
            "link": video_link,
            "published_date": published_date
        })
    
    return videos_data


def main():
    # Input YouTube channel URL
    channel_url = input("Enter the YouTube channel URL: ").strip()
    
    # Scrape the channel videos
    print("Scraping video data...")
    video_data = scrape_channel_videos(channel_url)
    
    if video_data:
        # Save to Excel
        output_file = "youtube_channel_videos.xlsx"
        df = pd.DataFrame(video_data)
        df.to_excel(output_file, index=False)
        print(f"Scraped data saved to {output_file}")
    else:
        print("No videos found or failed to scrape channel videos.")


if __name__ == "__main__":
    main()
