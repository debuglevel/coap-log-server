Small tool to log/view into requests sent to a CoAP server. Meant to be used with string payload (probably even UTF-8). No idea what happens if other payloads are sent.

# Requirements:
- Use with `python2`!
- Install dependencies with `pip install -r requirements.txt`

# Usage:
To start logging server on UDP port 1234, call `python2 coap-log-server.py -p 1234`. If no `-p` is given, standard port `5683` is used.

A request to this server can be sent via `python2 coap-client.py -o POST -P HelloWorld -p coap://localhost:1234/log`

The server will write this on STDOUT:
```
POST /: 'HelloWorld'
```
