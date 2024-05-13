# import requests                                                          
# from phone import numbers 
# # numbers = "+2349160196916"

# url = "https://textflow-sms-api.p.rapidapi.com/send-sms"

# payload ={  
# "phone_number":numbers,
# "Email_adress":"ibechinaecherem277@gmail.com",
# "text":"Hello boss how are you doing? i need 30 bellion from you now,i want you to send it now else."

# }
# headers = {
#     'content-type': 'application/json',
#     'X-RapidAPI-Key': 'b331bac727msh5505b72e1c12a3cp178abajsn63d38a08ec76',
#     'X-RapidAPI-Host': 'textflow-sms-api.p.rapidapi.com'
#   }


# response = requests.post(url, json=payload,headers=headers)
# print(response.json())


import requests

url = "https://textflow-sms-api.p.rapidapi.com/service/check"

payload = { "testing": "true" }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "8d8cf61798msh1a74451cf9b5b38p118272jsnecc1838c9022",
	"X-RapidAPI-Host": "textflow-sms-api.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())