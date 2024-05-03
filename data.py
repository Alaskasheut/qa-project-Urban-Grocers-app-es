#These are the headers required in a request
headers = {
    "Content-Type": "application/json",
   }

#Create a new user
user_body = {
    "firstName": "Alma",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

#Create kit
kit_body = {
    "name": "New kit",
    "card": 1 }

#This is an empty body to test if it is possible to create a kit with and empty body
kit_body_empty={}
