#!/bin/bash
curl -i -H "Content-Type: application/json" -X POST -d '{"position": 1 }' http://localhost:5000/fib
curl -i -H "Content-Type: application/json" -X POST -d '{"position": 4 }' http://localhost:5000/fib
curl -i -H "Content-Type: application/json" -X POST -d '{"position": 5 }' http://localhost:5000/fib
curl -i -H "Content-Type: application/json" -X POST -d '{"position": 8 }' http://localhost:5000/fib
curl -i -H "Content-Type: application/json" -X POST -d '{"position": 10 }' http://localhost:5000/fib
curl -i -H "Content-Type: application/json" -X POST -d '{"position": 40 }' http://localhost:5000/fib
curl -i -H "Content-Type: application/json" -X POST -d '{"position": 50 }' http://localhost:5000/fib
curl -i -H "Content-Type: application/json" -X POST -d '{"position": 100 }' http://localhost:5000/fib
