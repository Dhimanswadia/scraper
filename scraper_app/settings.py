# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import dj_database_url

BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['scraper_app.spiders']

ITEM_PIPELINES = ['scraper_app.pipelines.LivingSocialPipeline']

DATABASE = {
    'default': dj_database_url.config()
    'drivername': 'postgres',
    'host': 'ec2-54-225-223-40.compute-1.amazonaws.com',
    'port': '5432',
    'username': 'juagqzmyvhljvz',  # fill in your username here
    'password': 'H0GhC2nid4TcwYp1B76HMuQpFk',  # fill in your password here
    'database': 'd14s66eejpvrag'
}
