# Mumbai-Flats-Rent-Prediction

## Table of Content
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [Credits](#credits)

## Overview
This model will help you to predict rent of houses in various locations of Mumbai, depending upon your choice of desired house.

## Motivation
People having no knowledge or very little knowledge about the real eastate industry of the " City of Dreams- Mumbai" will get an easy access to rental expenses of the location and houses of their preferences. As this will give an idea about amount of rent to be spent, they can plan accordingly.

## Technical Aspect
This project is divided into three parts:
1. Training a machine learning model with the help of linear model. 
2. Building and hosting a Flask web app.
3. Building a simple UI using html & css
    - A user can choose an area in sqft,floor number and number of bedrooms .
    - A user can also choose Furnished/ semi furnished/ fully furnished and apartment type.
    - An option of choosing a location is mandatory
    - After providing the inputs prediction of rental expense of the given requirement will be shown.

## Installation
The code is written in jupyter notebook and flask server is written in spyder app, so in order to run this code in simpliest manner just download anaconda. 
If your machine doesn't support anaconda simply download jupyter notebook using python(cmd) and instead of spyder you can use visual studio.

## Run
1.Download the whole project 
2.Open server.py and util.py files in spyder 
3.Run server.py 
4.Open html file (app.html) and give specific inputs and see the prediction


## Directory Tree 
```
├── client 
│   ├── app.css
│   ├── app.html
│   ├── app.js
├── model
│   ├── columns.json
│   ├── Flats for Rent in Mumbai
│   ├── Flats for Rent in Mumbai (organized).py
│   ├── Flats_for_Rent_in_Mumbai_model.pickle
│   ├── prop_data_clean
├── server
│   ├── artifacts
│       ├── columns.json
│       ├── Flats_for_Rent_in_Mumbai_model.pickle
│   ├── server.py
│   ├── util.py

```

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/rsp25/Mumbai-Flats-Rent-Prediction/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/rsp25/Mumbai-Flats-Rent-Prediction/issues/new). Please include sample queries and their corresponding results.

## Technologies Used

1.pandas 
2.numpy
3.Linear model
  - Multiple Linear model
  - stats model.api
  - Lasso regressor

## Credits
- (https://www.youtube.com/channel/UCh9nVJoWXmFb7sLApWGcLPQ) - This project wouldn't have been possible without this channels playlist. It saved my enormous amount of time while building UI part. 
