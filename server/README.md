# Psykon

## Development Utils:

use `server/manager.py` script for setting up and running server during development.

```
./manager.py <command>
```

---
**doc**  
Produce html output of API reference.

**NOTE:** To use this command you need `apiDoc` to be installed on the system:

```
npm install apidoc -g
```

---
**jsons**  
Produce JSON schemas. Before running server this command
should be used in order to produce schemas needed to validate requests.

---
**admin**  
Create an admin account with username and password set to `admin`.
In order you could work with the server an admin account is needed to be created first.  
```
-r, --reset                If the account exists, reset its password and permissions
```

---
**init**  
It calls `doc`, `jsons`, `admin` commands in order

---
**setup**  
It calls `admin` commands in order

---
**run**  
Run server in debug mode at `0.0.0.0:8080`.  
```
-p PORT, --port PORT       run at custom port  
-s, --setup                call "init" command beforehand
```

---
**test**  
Run postman tests. You need `newman` package to be installed and also an instance of the flask app
to be running.

**NOTE:** In order to override the app configuration you can use `FLASK_APP_SETTINGS` environment
variable, which must point to a configuration file.
