import os
import googleapiclient.discovery

def get_most_popular_videos(api_key, channel_id, start_date, end_date, max_results=50):
    """
    Fetches the most popular videos from a YouTube channel within a specified date range.

    :param api_key: YouTube Data API key
    :param channel_id: ID of the YouTube channel
    :param start_date: Start date in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ)
    :param end_date: End date in ISO 8601 format (YYYY-MM-DDThh:mm:ssZ)
    :param max_results: Maximum number of results to retrieve (Default is 50)
    :return: List of popular videos with their IDs and titles
    """
    # Initialize YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    # Fetch videos uploaded in the specified date range and sort them by view count
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=max_results,
        publishedAfter=start_date,
        publishedBefore=end_date,
        order="viewCount"  # Sort by view count
    )
    response = request.execute()

    # Extract video IDs and titles from the response
    popular_videos = []
    for item in response.get('items', []):
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        popular_videos.append((video_id, video_title))

    return popular_videos

# Example usage:
if __name__ == "__main__":
    # Replace these with your API key and channel ID
    YOUR_API_KEY = 'YOUR_YOUTUBE_API_KEY'
    CHANNEL_ID = 'YOUTUBE_CHANNEL_ID'

    # Define the date range
    START_DATE = '2024-01-01T00:00:00Z'
    END_DATE = '2024-03-01T00:00:00Z'

    # Fetch and print the most popular videos
    popular_videos = get_most_popular_videos(YOUR_API_KEY, CHANNEL_ID, START_DATE, END_DATE)
    for video_id, title in popular_videos:
        print(f"{title} (Video ID: {video_id})")
# Placeholder file for the data_extraction module 
