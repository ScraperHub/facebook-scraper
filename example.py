// Import the Crawling API
const { CrawlingAPI } = require('crawlbase');
// Import fs module
const fs = require('fs');

// Set your Crawlbase token
const api = new CrawlingAPI({ token: 'YOUR_CRAWLBASE_JS_TOKEN' });

// URL of the Facebook page to scrape
const facebookPageURL = 'https://www.facebook.com/Alibaba.comGlobal/';

// options for Crawling API
const options = {
  format: 'json',
  ajax_wait: true,
  scroll: true,
  scroll_interval: 30,
};

// Get request to crawl the URL
api
  .get(facebookPageURL, options)
  .then((response) => {
    if (response.statusCode === 200) {
      // Parse the JSON response
      const responseBody = JSON.parse(response.body);
      const htmlContent = responseBody.body;

      // Write the HTML content to an HTML file
      fs.writeFile('output.html', htmlContent, (err) => {
        if (err) {
          console.error('Error writing to file:', err);
        } else {
          console.log('HTML content saved to output.html');
        }
      });
    }
  })
  .catch((error) => {
    console.error('API request error:', error);
  });
