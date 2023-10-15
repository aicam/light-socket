# Intallation
Python version > 3.6

# Contributions
##Ali Risheh:
- connect command
- list command
- terminate command
- send command
- Creating Server & Client Connections

---------------------------------------
## Jerome Pineda
- help command
- myport command
- myip command
- exit command
- Error handling

# Usage
The code can be run using the following command:
```bash
python3 main.py <port number> 
```
# Implementation
After running the code, it initialize 
a UDP socket server on the specified port and listens
to the incomming connections which is handled by `handle_client`
function. This function is running on a thread and is called
asynchronous to the main process. In this regard, you can
interact with the process using commands without need to
wait for incomming connections. <br>
`server_running` variable is used globally to stop threads
when the process is terminated. `clients` variable stores
the information of incomming connections and `servers` stores
UDP servers which the process is connected to. <br>
The core structure is based on running commands on a `while` loop
to get input from user and perform functionalities and 
handling connections in a thread. This architecture ensures
asynchronous connection. <br>
Socket is error-prone and needs error handling in every step.
In this regard, many `try` and `catch` are placed both in the
loop and in the functions internally.

