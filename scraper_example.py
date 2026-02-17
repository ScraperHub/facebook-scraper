"""
Facebook Scraper - Python Example
Extract valuable data from Facebook at scale using Crawlbase API
"""

from crawlbase import CrawlingAPI
import json

# Initialize API with your token
api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})


def scrape_facebook_page(page_url: str) -> dict:
    """
    Scrape a Facebook page.

    Args:
        page_url: The Facebook page URL to scrape

    Returns:
        dict: Scraped page data
    """
    response = api.get(page_url, {'scraper': 'facebook-scraper', 'format': 'json'})

    if response['status_code'] == 200:
        data = json.loads(response['body'])
        print(f"Page scraped: {data.get('name', 'N/A')}")
        return data
    else:
        raise Exception(f"Failed to scrape: {response['status_code']}")


def scrape_facebook_posts(profile_url: str, limit: int = 10) -> list:
    """
    Scrape Facebook posts from a profile or page.

    Args:
        profile_url: Facebook profile/page URL
        limit: Max number of posts to retrieve

    Returns:
        list: List of post data
    """
    response = api.get(profile_url, {
        'scraper': 'facebook-scraper',
        'format': 'json',
        'post_limit': limit
    })

    if response['status_code'] == 200:
        data = json.loads(response['body'])
        posts = data.get('posts', [])
        print(f"Scraped {len(posts)} posts")
        return posts
    else:
        raise Exception(f"Failed to scrape posts: {response['status_code']}")


def batch_scrape(urls: list) -> list:
    """
    Batch scrape multiple Facebook URLs.

    Args:
        urls: List of Facebook URLs

    Returns:
        list: Results for each URL
    """
    results = []

    for url in urls:
        try:
            data = scrape_facebook_page(url)
            results.append({'url': url, 'success': True, 'data': data})
        except Exception as e:
            results.append({'url': url, 'success': False, 'error': str(e)})

    return results


def export_to_json(data: any, filename: str) -> None:
    """Save scraped data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Data saved to {filename}")


if __name__ == '__main__':
    example_url = 'https://www.facebook.com/example-page'

    try:
        page_data = scrape_facebook_page(example_url)
        export_to_json(page_data, 'facebook_page.json')
        print("Scraping completed successfully!")
    except Exception as e:
        print(f"Error: {e}")
