# QA PROJECT URBAN GROCERS
## Testing create_kit

This project consists in test cases for the field "name" in the body for a request to create a new kit for a user.

#  The requirements for test cases follow the documentation find in:
```ssh 
Apidocs    URL/docs/
```
```ssh 
Swagger    URL/api/swagger
```

# Requeriments
- It is neccesary to previously install pytest and request packages to execute the test cases.
- After install the mentioned packages the test file must be configurated with pytest.

# Tests for 'name' parameter to create a kit for an user

| ID | Test | 
| ------ | ------ |
| 1 | Minimum number of characters (1) |
| 2 | Maximum number of characters (2) |
| 3 | The number of characters is less than the allowed amount (10) |
| 4 | The number of characters is more than the allowed amount (512) |
| 5 | Special characters are accepted |
| 6 | Spaces are accepted |
| 7 | Numbers are accepted |
| 8 | The parameter do not pass the request |
| 9 | A different parameter is used (a number data type instead an string data type)d |

## Urban Grocers [ create_kit - parameter: "name" ] testing checklist

[File tests Project Urban Grocers](https://docs.google.com/spreadsheets/d/1MMni-gecUXFTzBP6Q6ReykiM-AhpKyG6/edit?usp=drive_link&ouid=112711575793272570934&rtpof=true&sd=true)

