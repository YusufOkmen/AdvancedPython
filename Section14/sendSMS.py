import vonage

client = vonage.Client()
       

responseData = client.send(
    {
        "from": "Deneme",
        "to": "905393263963",
        "text": "This message send my Python programme" 
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")