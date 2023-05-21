import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

# Define script defaults
DEFAULT_WAIT_SECONDS = 10
DEFAULT_URL = "https://developer.salesforce.com/docs/marketing/pardot/guide/error-codes.html"
DEFAULT_ROOT_ELEMENT = "doc-content-layout"

# Configure script arguments
parser = argparse.ArgumentParser(
    prog = "WebScraper",
    description = "Simple web scraper",
    formatter_class = argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument("-u", "--url", help = "URL to scrape", default = DEFAULT_URL)
parser.add_argument("-r", "--root-element", help = "Root element to scrape for text on the given URL", default = DEFAULT_ROOT_ELEMENT)
parser.add_argument("-w", "--wait", help = "Period in seconds to wait for the given URL to render", default = DEFAULT_WAIT_SECONDS)

# Parse script arguments
args = parser.parse_args()
wait = args.wait 
url = args.url 
root_element = args.root_element 

# Configure browser options
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Create browser
driver = webdriver.Chrome(options = options) 
driver.implicitly_wait(wait)  

# Request web page
driver.get(url)  

# Print contents of the root element
element = driver.find_element(By.TAG_NAME, root_element)
print (element.text)

# Shutdown browser
driver.quit()
