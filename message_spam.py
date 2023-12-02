import requests
import time

tokens = ["MTE0Mjk1MzE3MzAxMTY2OTA5Mg.GzVmUU.C3bvpnpZioiC7sX0Bs5eReeSGklmfsOxhK2kq0", "MTE4MDM2Mzg3MjE4NDU3ODEyOQ.GsGuvw.1ZQSj-wG4V1zLbx8eKO_6yeMBFrkkrhYngBuBc"]
url = "https://discord.com/api/v9/channels/1180593865846173708/messages"
data = {
    "content": "test"
}

while True:
    for token in tokens:
        headers = {
            "Authorization": f"Bot {token}",
            "Content-Type": "application/json",
        }

        response = requests.post(url, json=data, headers=headers)

        print(f"Response for {token}:")
        print(response.status_code)
        print(response.json())  # If your server returns JSON response, otherwise omit this line
        print("\n---\n")

        # Add a delay between sending messages with different tokens
        time.sleep(3)  # Sleep for 5 seconds before sending the next message

    # Add a longer delay before restarting the loop
    time.sleep(2)  # Sleep for 60 seconds before the next iteration
