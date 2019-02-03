#!/bin/bash
docker build -t kbsrunschi/my-fibonacci-app .
docker run -p 5000:5000 --rm -t kbsrunschi/my-fibonacci-app
