# SCOTTURBapp
A mobile app to check SCOTTURB bus schedules. 
You can find them at http://www.scotturb.com/carreiras/horarios/.

## How is the project being organized?
I'm trying to devide the project in 3 microservices using (and learning how to use) Docker:
 - One that will fetch all the data from http://www.scotturb.com/carreiras/horarios/verao;
 - A DB.
 - A webserver (I'm thinking of using lumen) to construct an API that the mobile app will consume.

### Web Scraping
The webscraping tool I will be using Beautiful Soup - https://www.crummy.com/software/BeautifulSoup/bs4/doc/. It is my first time using it, so I will be learing it as well.
I'm thinking of mounting this service in a Docker container and configuring it to periodically check if there has been changes in scotturb's websit. If so, it'll scrap it.

### Database
I will be storing all the data in a mysql DB.

### API
I'm thinking of using a framework to offer an API for the mobile app to consume. Maybe I'll use a PHP framework named Lumen.

## Project status
Some phases:
 - Data scraping from scotturb's site - DOING;
 - API development;
 - Mobile app development;
 
