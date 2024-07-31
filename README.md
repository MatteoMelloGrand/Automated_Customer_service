# Automated_Customer_service

Hello to everyone, this is a project consisting on building an automated customer service for ecommerces, small businesses and every website which deals with customers.
The idea of this project is of to evaluate the limits of application of large language models to customer service, and so evaluating which are the duties of a customer assistant that cannot be automated using artificial intelligence.

# Technologies used
The technologies used in the project are:\
For front-end: HTML, CSS\
For back-end: Python, Django, React\
For the large language model: GOT-3/Llama 3.1

# How the automated service is set
The way of how I decided to set the system is the following:
SUppose that a client asks a question to the customer service, the question is then inserted in a pre-built document which tells exactly to the LLM all the details about the product that is being sold and how to repply to the questions.
The informations contained in the document are:
1) Dimensions, weight, and specifics about the product
2) Price of the product and of bundles, disocunts...
3) List of the products in sale
4) Refund policies
5) Shipping details (timings, prices...)

Moreover, the document shoud include some indications on how to behave in front of certain situations. For example:
1) How to behave when asked about the shipping details
2) How to behave when asked to speak with a human
3) How to behave when asked a refund
4) How to promote the product if someone is interested in buying it

You can find an example of the document in the repository.
