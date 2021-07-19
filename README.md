# Recommendation System - Hepsiburada


#### Table of Contents  

- [About](#About)
- [Datasets](#Datasets)
- [Dependencies](#Dependencies)
- [Usage](#Usage)
- [Running The API Example](#API-Example)


## About <a name="About"></a>

In this repo, I tackled a challenge from Hepsiburada. The challenge is building a related products recommendation for the cart page of an online store. Meaning that when a customer is landed on the cart page, a list of recommended products should be provided. 



## Datasets <a name="Datasets"></a>

- **Events.json:** contains events of type 'cart', adding a product to the cart.
- **Meta.json:** contains info about the products. 


## Dependencies <a name="Dependencies"></a>

To run the notebook: 

- pandas==1.1.3
- gensim==4.0.1
- sklearn
- json
- string

To run the API example: 

- pandas==1.1.3
- requests==2.21.0
- Flask==1.1.2
- json


## Usage <a name="Usage"></a>

The repo contains a comprehensive [**notebook**](../main/notebook.ipynb) that I recommend starting with.

There is also a [**Design Document**](../main/design_document) provided, which discusses some of the things in the notebook in more detials and also the futuer work.

Other than that, an **API** is added for the sake of providing an example request as required int the challenge. Check it out only if you are interested, but the notebook is already detailed enough to help in understanding the methods implemented.  

## Running The API Example <a name="API-Example"></a>

To run the [API Example](../main/api_example):

1. first need to run the notebook. Running the notebook will invove **pickling** some objects that are used on the server. Make sure the datasets (json files) exist in the cwd in a directory called **data**.
2. start the flask server and leave it open.
```
python3 api_example/flask_api.py
```
3. run the examples.py script and wait for a response from the server.
```
python3 api_example/examples.py
```





