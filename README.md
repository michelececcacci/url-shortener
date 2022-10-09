# url-shortener
[![codecov](https://codecov.io/gh/michelececcacci/url-shortener/branch/main/graph/badge.svg?token=04TBME77VL)](https://codecov.io/gh/michelececcacci/url-shortener)
[![Django CI](https://github.com/michelececcacci/url-shortener/actions/workflows/django.yml/badge.svg)](https://github.com/michelececcacci/url-shortener/actions/workflows/django.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/michelececcacci/url-shortener/badge/main)](https://www.codefactor.io/repository/github/michelececcacci/url-shortener/overview/main)

Url shortener that uses a randomized algorithm and guarantees up to 2 billion unique ids based, with a fixed 6-character url short id. 
Built using Django and Postgresql. 

The project deployed on Heroku, but not anymore since Heroku has cut free hosting. 

Added sentry support to track failures both in production and in development environments. 

API ROUTES (must be added to base url):
```
/<short_link>
```
Simulates a click, incrementing the click count by 1, and returns the long link, short link and addition date of the link.
```
/api/
```
Retrieves all the links and all their informations
```
/api/add/
```
Allows to add a custom url (using the long field) and shortens it
```
/api/infos/<short_link>
```
Grabs infos about corresponding shortened link, but does not increment the click count.
