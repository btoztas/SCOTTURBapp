# SCOTTURBapp
A mobile app to check SCOTTURB bus schedules. 
You can find them at http://www.scotturb.com/carreiras/horarios/.

## How is the project being organized?
I'm trying to devide the project in 3 microservices using (and learning how to use) Docker:
 - One that will fetch all the data from http://www.scotturb.com/carreiras/horarios/verao;
 - A DB.
 - A webserver (I'm thinking of using lumen) to construct an API that the mobile app will consume.
