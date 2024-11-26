import base64

# Open the service account file in binary mode
with open("newserviceAccountKey.json", "rb") as file:
    # Read the content and encode it into base64
    encoded = base64.b64encode(file.read()).decode('utf-8')

# Write the encoded content to a new file or print to the console
with open("serviceAccountKey.base64", "w") as encoded_file:
    encoded_file.write(encoded)

# Optionally, print the encoded value
print(encoded)
