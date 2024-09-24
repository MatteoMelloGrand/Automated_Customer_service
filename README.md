# Automated_Customer_service

Hello to everyone, this is a project consisting on building an automated customer service for ecommerces, small businesses and every website which deals with customers.
The idea of this project is to evaluate the limits of application of large language models to customer service, and so evaluating which are the duties of a customer assistant that cannot be automated using artificial intelligence.

# Technologies used
The technologies used in the project are:\
For front-end: HTML, CSS, Javascript\
For back-end: Python, Flask\
For the large language model: Llama 3.1

# How the automated service is set
The way of how I decided to set the system is the following:
Suppose that a client asks a question to the customer service, the question is then inserted in a pre-built document which tells exactly to the LLM all the details about the product that is being sold and how to reply to the questions.
The informations contained in the document are:
1) Dimensions, weight, and specifics about the product
2) Price of the product and of bundles, discounts...
3) List of the products in sale
4) Refund policies
5) Shipping details (timings, prices...)

Moreover, the document should include some indications on how to behave in front of certain situations. For example:
1) How to behave when asked about the shipping details
2) How to behave when asked to speak with a human
3) How to behave when asked a refund
4) How to promote the product if someone is interested in buying it

You can find an example of the document in the repository.
In this way, the system should be able to reply correctly to most of the questions that a customer can make.



# Limits encountered
The limits encountered in the development of the project are the following:
1) Decision making\
   for some actions, such as determining wheter giving a refund or not, it is better the intervention of a human. Indeed, considering the example of the refund,  the LLM is not still able to evaluate wheter a refund inquiry is a fraud or not.
2) Health/sensitive informations\
   Some products, such as food, can cause serious health problems if in presence of an allergy. Therefore, a common question to the customer service could be if the product is suggested to people with a certain patology or allergy. Giving to the LLM the total responsability for deciding wheter a product is suitable or not is too risky. Suppose for example that a celiac man asks to the LLM if a certain food sold in the ecommerce can be eaten by celiacs. If the LLM reply that it is, then the man could have serious health problems.
