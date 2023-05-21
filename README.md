# web-scraper
```shell
usage: WebScraper [-h] [-u URL] [-r ROOT_ELEMENT] [-w WAIT]

Simple web scraper

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL to scrape (default: https://developer.salesforce.com/do
                        cs/marketing/pardot/guide/error-codes.html)
  -r ROOT_ELEMENT, --root-element ROOT_ELEMENT
                        Root element to scrape for text on the given URL (default:
                        doc-content-layout)
  -w WAIT, --wait WAIT  Period in seconds to wait for the given URL to render
                        (default: 10)
```