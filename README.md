# Socket-Based Communication Server  

Welcome to "Socket-Based Communication Server". I created a small server using Python sockets for my home server. This is just the tip of the iceberg. I'm continuously working on this to make it bigger and more useful.

Table of Conetens
- [Requirements](#requirements)
- [Setup the Server](#setup-the-server)
- [Server in Action](#server-in-action)

## Requirements

![Requests Version](https://img.shields.io/badge/Requests-2.26.0-red) ![Python](https://img.shields.io/badge/Python-3.12.0-green) ![Pip](https://img.shields.io/badge/Pip-24.0-blue) ![Countryinfo](https://img.shields.io/badge/Countryinfo-0.1.2-purple)

## Setup the Server

Clone the github report to your system.

```bash
git clone https://github.com/bericontraster/Socket-Based-Communication-Server.git
```  
  
Installing the dependencies.  
   
```bash
python3 -m venv virt
source virt/bin/activate
pip3 install -r requirements.txt
```

Once everything is setup run the server using python3.

```bash
~$ python3 server.py
PRESS [ENTER] TO POWERON ZI$CORD
ZI$CORD PLUGGED IN ('127.0.1.1', 5050)
```
  
The server will power on and display the port and IP to which the client can connect. Before connecting to the server manually change the IP of the `client.py` file.

## Server in Action

While the server is running, connect to the server using client.

![Server Connect](/img/server-connect.png)

Fetching Countries Information using API calls and displaying received json data. i.e `fetch-countryname`

![Fetch Country Info](/img/country-info.png)

Getting random qoute using [ZenQuotes](https://zenquotes.io/) API. i.e `qoute`

![Qoutes](/img/qoute.png)