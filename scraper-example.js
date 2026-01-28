// Example: Facebook Scraper using Crawlbase API

const { CrawlingAPI } = require('crawlbase');

// Initialize the API with your token
const api = new CrawlingAPI({ token: 'YOUR_CRAWLBASE_TOKEN' });

/**
 * Scrape a Facebook page
 */
async function scrapeFacebookPage(pageUrl) {
  try {
    const response = await api.get(pageUrl, {
      scraper: 'facebook-scraper',
      format: 'json'
    });
    
    console.log('Page data:', JSON.parse(response.body));
    return JSON.parse(response.body);
  } catch (error) {
    console.error('Error scraping page:', error);
    throw error;
  }
}

/**
 * Scrape Facebook posts from a profile
 */
async function scrapeFacebookPosts(profileUrl, limit = 10) {
  try {
    const response = await api.get(profileUrl, {
      scraper: 'facebook-scraper',
      format: 'json',
      post_limit: limit
    });
    
    const data = JSON.parse(response.body);
    console.log(`Scraped ${data.posts.length} posts`);
    return data.posts;
  } catch (error) {
    console.error('Error scraping posts:', error);
    throw error;
  }
}

/**
 * Batch scrape multiple Facebook URLs
 */
async function batchScrape(urls) {
  const results = [];
  
  for (const url of urls) {
    try {
      const data = await scrapeFacebookPage(url);
      results.push({ url, success: true, data });
    } catch (error) {
      results.push({ url, success: false, error: error.message });
    }
  }
  
  return results;
}

// Example usage
if (require.main === module) {
  const examplePageUrl = 'https://facebook.com/example-page';
  
  scrapeFacebookPage(examplePageUrl)
    .then(data => {
      console.log('Successfully scraped page!');
    })
    .catch(error => {
      console.error('Failed to scrape page:', error);
    });
}

module.exports = {
  scrapeFacebookPage,
  scrapeFacebookPosts,
  batchScrape
};
