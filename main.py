"""
IN this project we will learn about post,put ,delte and also learn about authentication using headers
"""
import requests

from user_account_details import UserDetails

pixela_api_endpoint = "https://pixe.la/v1/users"

user_details = UserDetails()
# these are a parameter required to create new account on pixela
user_params = {
    "token": user_details.token,
    "username": user_details.username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
"""Note:
we have get ,post,put,delete http requests for fetch and sending data to or from sever.
Get request => It is used for fetching a data from api_endpoint.
for eg: requests.get(url=apiendpoint_url,params=parameters)

Post request=> used to send a data to a external service (server) and it take data in json format.
for eg :  requests.post(url=apiendpoints,json = parameters)

Put requests=> used to update an existing data on server

Delete request => used to delete an existig data.
"""
# creating account using Post method
"""we send our data in form  of json format to a server"""
# response = requests.post(url=pixela_api_endpoint,json=user_params)
# response.raise_for_status()
# print(response.text)

"""Create a new pixelation graph definition."""
graph_endpoint = f"{pixela_api_endpoint}/{user_details.username}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Exercise Graph",
    "unit": "hours",
    "color": "ajisai",
    "type": "int",
}
# For authenticate ourselves pixela take auth-token same like login your account so we have to pass headers
headers = {
    "X-USER-TOKEN": user_details.token
}

response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
response.raise_for_status()
print(response.text)

# Post a pixel on a graph basically adding a data to a graph on specific date.
graph_id = "graph1"
