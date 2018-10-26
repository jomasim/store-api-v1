# store-api-v1
[![Build Status](https://travis-ci.com/jomasim/store-api-v1.svg?branch=dev)](https://travis-ci.com/jomasim/store-api-v1)
[![Coverage Status](https://coveralls.io/repos/github/jomasim/store-api-v1/badge.svg?branch=dev)](https://coveralls.io/github/jomasim/store-api-v1?branch=dev)
[![Maintainability](https://api.codeclimate.com/v1/badges/9a1ccecdb84a694bf64b/maintainability)](https://codeclimate.com/github/jomasim/store-api-v1/maintainability)

This is v1 of Restful API to power store-manager front-end pages
The API is available at [https://store-api-22.herokuapp.com/](https://store-api-22.herokuapp.com/)

# Requirements
- `python3` - [Python](https://www.python.org/)
- `pip` - [Install pip](https://pip.pypa.io/en/stable/installing/)
- `virtualenv` - [install virtualenv](https://virtualenv.pypa.io/en/stable/installation/)


# Endpoints
| Http Method | Route | Functionality |
| ----------- | ----- | ------------- |
| POST        | /api/v1/auth | user login|
| POST        | /api/v1/user | create user|
| GET         | /api/v1/products | gets all products |
| GET         | /products/productId| get a product by prodcutId |
| GET         | /api/v1/sales |gets all sales |
| GET         | /api/v1/sales/saleId| gets sale record by saleId |
| POST        | /api/v1/products| gets all products |
| POST        | /api/v1/sales | gets all sales |


# Setup 

clone repo from github

- `$ git clone https://github.com/jomasim/store-api-v1.git`
- `$ cd store-api-v1`
- `$ git checkout dev `

Create a virtual environment

`$ python3 -m venv venv`

Activate the virtual environment

`$ . venv/bin/activate`

Install project dependencies

`$ pip install -r requirements.txt`

Running app

`$ python3 run.py `

# Running tests
`$ pytest tests`

# Documentation

Find api doumentation [here](https://documenter.getpostman.com/view/3224897/RzZ1q2wN)

# Framework 
Python Flask 
