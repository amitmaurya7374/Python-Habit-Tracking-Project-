"""
IN this project we will learn about post,put ,delte and also learn about authentication using headers
"""
import requests

from user_account_details import UserDetails

user_details = UserDetails()
TOKEN = user_details.token
USERNAME = user_details.username
GRAPHID = "graph1"

pixela_api_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_api_endpoint}/{USERNAME}/graphs"

# these are a parameter required to create new account on pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME,
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
# graph_params = {
#     "id": "graph1",
#     "name": "Exercise Graph",
#     "unit": "hours",
#     "color": "ajisai",
#     "type": "int",
# }
# # For authenticate ourselves pixela take auth-token same like login your account so we have to pass headers
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# response.raise_for_status()
# print(response.text)

# Post a pixel on a graph basically adding a data to a graph on specific date.
# pixel_creation_endpoint = f"{pixela_api_endpoint}/{USERNAME}/graphs/{GRAPHID}"
# today = datetime.now()
#
# pixel_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "10",
#     "optionalData": '{"body_part":"upper_part"}'
# }
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# response.raise_for_status()
# print(response.text)

# update a pixel
pixel_update_endpoint = f"{pixela_api_endpoint}/{USERNAME}/graphs/{GRAPHID}/20210302"
# pixel_update_data = {
#     "quantity": "20",
# }
# response = requests.put(url=pixel_update_endpoint,json=pixel_update_data,headers=headers)
# response.raise_for_status()
# print(response.text)

# Delete a pixel from a specific date
response = requests.delete(url=pixel_update_endpoint,headers=headers)
response.raise_for_status()
print(response.text)
