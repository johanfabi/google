# Import libraries
import requests

# Define the webhook URL
webhook_url = 'https://chat.googleapis.com/v1/spaces/AAAAwZW8VKw/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=merXwhOCefIxOmu5bHt8R0_MaclFxK8ShWF7cjIVufw'


# Define the message
message = {
    "text": "This is a message from my Python script!"
}

# Send the message to the webhook URL
response = requests.post(webhook_url, json=message)

# Check if the message was sent successfully
if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Error sending message: {response.status_code}")
    


