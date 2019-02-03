# README

# Fibonacci Application

## How to run the test suite

    ubuntuAWS$ python -m unittest discover .

## Deployment instructions

[ ] Log into AWS ec2 instance with port forwarding

    localMachine$ ssh -i {YOUR PEM}.pem -L 5000:127.0.0.1:5000 ubuntu@54.227.81.4

[ ] cd into fibonacci_app repo and pull the latest

    ubuntuAWS$ cd fibonacci_app
    ubuntuAWS$ git pull

[ ] Build & Deploy docker app

    ubuntuAWS$ docker build -t kbsrunschi/my-fibonacci-app .
    ubuntuAWS$ docker run -p 5000:5000 --rm -t kbsrunschi/my-fibonacci-app

Alternatively, run both of these commands via the startup script

    ubuntuAWS$ sh docker_up.sh

[ ] On your local machine, use any of the following commands to test your connection to the application

    curl -i http://localhost:5000/

    curl -i http://localhost:5000/fib

    curl -i http://localhost:5000/fib/help

[ ] Populate some base data (requires cloning the git repo locally) with the application running on the AWS instance

    git clone https://github.com/kbsrunschi/fibonacci_app.git

    cd fibonacci_app

    sh populate_data.sh

## Using the application

  See all previously computed fibonacci numbers
    curl -i http://localhost:5000/fib

  See available commands
    curl -i http://localhost:5000/fib/help

  Get the fibonacci number for some number position in the sequence n
    curl -i -H "Content-Type: application/json" -X POST -d '{"position": {n} }' http://localhost:5000/fib

  Delete the value associated with the position in the sequence n
    curl -X "DELETE" http://localhost:5000/fib/{n}

## Stop all instances

    ubuntuAWS$ sh docker_down.sh

## Data persistence

This application does not use a database to store historical fibonacci numbers viewed, instead relying on a memory data structure. This means that when the server is stopped, all prior data will be lost. 
In order to speed up testing and/or usage of this application, there is a script `populate_data.sh` that can be called to populate some base values.

## Security

I did not add authentication to this application but doing so would be simple with the help of flask's HTTPBasicAuth library.

## Improvements

Given a more complex application, I would add a Drakefile to automate pushing and pulling Docker images, the set up of a database and dependent containers, and shorthand commands to build, test, start, and exec into the container images. Nginx and Gunicorn could be added to support high traffic.

# Feature/Flow Refactor

### Product Display & Caching

Currently, from the Homepage a customer can scroll to the SHOP BY CATEGORY section and select a category.

From there, the page is slow to load so I would speed up the code and infrastructure to return the items in under 1 second.

Next, the user has a different experience on the next screen depending on what category they selected
* For WINE, a user can FILTER BY Canned/Red/Rose & Sparkling/White before going to the Product page, whereas all other categories go straight to the Product page.

From there, a user cannot VIEW ALL for the entire category (Say WINE or SNACKS & SWEETS) and must click in each sub category (e.g CHIPS, DIPS, SALTY SNACKS under SNACKS & SWEETS) to see all the products. This is incredibly time consuming and does not let the user compare and contrast items for a faster checkout. I would add a VIEW AS ONE (or something similar) to each category that lets you see all sub category products in one continuous page. 

Additionally, the user cannot filter within this sub category to narrow the choices and have a faster checkout. I would add a filter to the top of each category that was already restricted to the category the user is shoping in for faster item selection.

Additionally, the number of previews for each sub category are not consistent even when there are enough products to show a consistent number of previews. Eg Fruis & Veggies only displays 2 preview items where as Charcuterie & Cheese displays 8 before seeing the VIEW ALL card. 

The benefit of making these changes is a consistent experience so the user knows what to expect and a faster checkout when they are looking for a specific item rather than browsing. A faster checkout has the potential to mean a smaller basket but it also retains customers who would have gotten annoyed at not being able to find what they were looking for and not purchasing on Foxtrot at all.

### Recommendations

Currently, Foxtrot does not recommend any products either while viewing an item or after adding the item to my basket.

I would add product recommendations that can be immediately added or viewed from the current product page. This gives the user the option of learning more about the complementary product or immediately adding the product, both of which will increase the likelihood of a bigger basket.  Its important to allow the user to both immediately add the item to their basket or view the item to improve customer satisfaction while using our serivce. 

### Historical Purchases

Foxtrot does not store historical purchases on the user profile. I would add a screen somewhere from the Perks/Account page (5th icon in the dock) that lets users view their recent purchases and auto-add the prior order to their basket. 

From the home screen, I would also add a "Order Again" banner that users could click to view their most recent purchase and add the items to the cart. Users know what they like and if they really enjoyed a bundle, they will be more likely to order it again if (1) they can remember all the items and (2) its easy for them to rebuild that basket. This flow will drive more sales since users like reordering what they know and love. 

### Better tagging

A lot of products aren't tagged well which causes users to miss out on items that they would otherwise be interested in purchasing. An example of this is searching _vegan_ returns approx 10 results, notably not including guacamole. When I view the guacamole item, it is labelled vegan. Improved tagging will enable users to find what they are looking for faster and increase number of completed purchases. 


## Overall

By speeding up the pages both by adding caching and improving the application response time, and improving the searching and viewing of items, we can increase the size of a users basket and improve user completion rates driving higher sales. 

