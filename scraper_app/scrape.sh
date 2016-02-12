#!usr/bin/env bash

# be sure to change both virtualenv directory and scrape/living_social
# directory to where your venv and code is.
source $WORKON_HOME/scrape/bin/activate
cd /Projects/new-coder/scrape_workspace/my_scraper/scraper_app
scrapy crawl livingsocial
