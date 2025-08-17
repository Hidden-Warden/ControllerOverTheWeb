# ControllerOverTheWeb
A client side and a server side python script to send/reiceve controller inputs over the web.

Steps to run the project:

Download the project and extract the files.

# Run the client (for your friend)
Open a PowerShell window, and paste the following command to install the required libraries:
(Be sure to have python installed on your system.)
```pip install pygame```

Then run the client.py file using the following command:
```python client.py```

Then, they will be prompted to enter the IP address and port of the server they want to connect to. They can enter the IP address and port of the server you are hosting.

The IP can also be a domain name, if you have one set up to point to your server/router.

# Run the server (for you hosting the game)
Open a PowerShell window, and paste the following command to install the required libraries:

Run the Firewall-Script.ps1 script to allow the server to communicate through the firewall: (Make sure to run PowerShell as an administrator)
```powershell.\Firewall-Script.ps1```

Then run the server.py file using the following command:
```python server.py```

# Troubleshooting
If you want user from outside your network to connect to your server, you need to port forward the port XXX on your router. You can use NAT to do this.

Exemple: If your server is running on port 6000, you need to forward port 6000 on your router to the local IP address of the machine running the server.py script.