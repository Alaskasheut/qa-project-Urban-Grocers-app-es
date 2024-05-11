import configuration
import requests
import data

#Create a new user
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,json=body,headers=data.headers)

#Create a new kit in an client account
def post_create_new_client_kit(kit_body,auth_Token): #
    current_headers=data.headers.copy()
    current_headers['Authorization'] = "Bearer " + auth_Token
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=kit_body,headers=current_headers
    )





