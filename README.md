# README

# Fibonacci Application

## Table of Contents
1. [Testing](#testing)
2. [Deploying](#deployment)
3. [Using the app](#running)
4. [Tear down docker](#teardown)
5. [iOS App Refactor](#feature_refactor)

## How to run the test suite <a name="testing"></a>

    ubuntuAWS$ python -m unittest discover .

## Deployment instructions <a name="deployment"></a>

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

    localMachine$ curl -i http://localhost:5000/

    localMachine$ curl -i http://localhost:5000/fib

    localMachine$ curl -i http://localhost:5000/fib/help

[ ] Populate some base data (requires cloning the git repo locally) with the application running on the AWS instance

    localMachine$ git clone https://github.com/kbsrunschi/fibonacci_app.git

    localMachine$ cd fibonacci_app

    localMachine$ sh populate_data.sh

## Using the application <a name="running"></a>

  See all previously computed fibonacci numbers
    localMachine$ curl -i http://localhost:5000/fib

  See available commands
    localMachine$ curl -i http://localhost:5000/fib/help

  Get the fibonacci number for some number position in the sequence n
    localMachine$ curl -i -H "Content-Type: application/json" -X POST -d '{"position": {n} }' http://localhost:5000/fib

  Delete the value associated with the position in the sequence n
    localMachine$ curl -X "DELETE" http://localhost:5000/fib/{n}

## Stop all instances <a name="teardown"></a>

    ubuntuAWS$ sh docker_down.sh

## Data persistence

This application does not use a database to store historical fibonacci numbers viewed, instead relying on a memory data structure. This means that when the server is stopped, all prior data will be lost. 
In order to speed up testing and/or usage of this application, there is a script `populate_data.sh` that can be called to populate some base values.

## Security

I did not add authentication to this application but doing so would be simple with the help of flask's HTTPBasicAuth library.

## Algorithm Performance

My Fibonacci algorithm caches in order to speed up the calculation of the value, and checks the hash of previously calculated values before performing the calculation to improve the performance from O(2^n) to O(logn).

## Improvements

Given a more complex application, I would add a Drakefile to automate pushing and pulling Docker images, the set up of a database and dependent containers, and shorthand commands to build, test, start, and exec into the container images. Nginx and Gunicorn could be added to support high traffic. Lastly, I would add a database to persist data between sessions and some frontend code to enable uses to view this tool in their web browser. 

# Feature/Flow Refactor <a name="feature_refactor"></a>

[iOS Application Review](https://docs.google.com/document/d/1Wz6OXJyaS4VLgTQVaLB1bUPthp_gLwyllmiiUb-IEoA/edit?usp=sharing)

