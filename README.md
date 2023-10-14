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
UDP servers which the process is connected to.
