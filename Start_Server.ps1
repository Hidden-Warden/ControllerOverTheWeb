Start-Process cmd.exe -ArgumentList '/k python.exe .\server.py'
Start-Process cmd.exe -ArgumentList '/k python.exe .\webserv_bridge.py'
Start-Process cmd.exe -ArgumentList '/k python.exe .\webserv.py'