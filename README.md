# url-shortener
Url shortener that uses a randomized algorithm and guarantees up to 2 billion unique ids based, with a fixed 6-character url short id. 

Built using Django and Postgresql. 

Project deployed on Heroku. 

Reached 95% code coverage.

Added sentry support to track failures both in production and in development environments. 

API ROUTES (must be added to base url):
```
/
```
Retrieves the 5 most clicked links
```
/api/
```
Retrieves all the links and all their informations
```
/api/add/
```
Allows to add a custom url (using the long field) and shortens it
