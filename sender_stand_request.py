import configuration
import requests
import data

#----------------------------------------POST----------------------------------------

#Create a new user

def post_new_user(body): #First, it is declared the function to request a new user creation.
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,json=body,headers=data.headers) # Path to post is given

#response=post_new_user(data.user_body) // to keep the value returned by post_new_user function
#print(response.status_code) // to print status code returned in request
#print(response.json()) // to print content 'authToken'

#Create a new kit in an client account
def post_create_new_client_kit(kit_body,auth_Token): #To create a kit the function requires two parameters: body--kit_body and token.
    current_headers=data.headers.copy() #Data.headers it copied to not alterated the original body.
    current_headers['Authorization'] = "Bearer " + auth_Token #Then, the authorization text is added with "Bearer " adding the token given when a new user is created.
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=kit_body,headers=current_headers
    )
#response_kit=post_create_new_client_kit(data.kit_body,response.json()["authToken"]) //This is an example with the variable response in a new_user.
#print(response_kit.status_code) //To verify the status, if the request was sucessfull
#print(response_kit.json()) //To verify the content







