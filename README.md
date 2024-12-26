# GTFY 🚀

[![docker-image](https://github.com/sanwebinfo/gtfy-listener/actions/workflows/docker.yml/badge.svg)](https://github.com/sanwebinfo/gtfy-listener/actions/workflows/docker.yml)  

Gotify to `Ntfy.sh` forwarder. This includes a few corrections and focuses on a http connection on a homeserver. This works from my Proxmox Server to Gotify to NTFY.

Forward Gotify Push Messages 🚀 to `Ntfy.sh` Push server by using websocket 🛸

using Gotify stream to Listen the Gotify Push Notifications via websocket Connection and Froward it to Ntfy Push server.

## Setup

```sh
git clone https://github.com/bertotuxedo/gtfy2ntfy
cd gtfy2ntfy
```

- Env File `.env`

```sh
nano .env
```

```sh
NTFY = "<NTFY Push server URL without HTTP(S)>" 
GOTIFY_HOST = "<http://Gotify host URL:Port/secrettopic>"
GOTIFY_TOKEN = "<GOTIFY CLIENT TOKEN>"
```

Example:
GOTIFY_HOST="192.168.10.48:8181"
NTFY_HOST="http://192.168.10.48:8180/mysupersecrettopic"
GOTIFY_TOKEN="CRpwR023ONqPR9D"

In this example both Gotify and NTFY are running on the same machine with different ports. 
Retreive Gotify token from the UI under "clients".
Save the .env with ctrl+O, Y, crtl+X

## Docker 🐬

Keep Running the Python Script in Docker  

- Update the `.dockerfile` before build - Replace example `ENV` with yours

```sh
nano Dockerfile
```

```sh
# Remove anything after octothorpe in entire script
# This is my current working configuration for HTTP to HTTP on a home server
FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip3 install requests python-dotenv websocket-client
ENV GOTIFY_HOST=XXX.XXX.XXX.XXX:XXXX    # URL of Gotify without leading HTTP
ENV GOTIFY_TOKEN="TOKENINQUOTES"   # Client Token from Gotify App
ENV NTFY_HOST=http://XXX.XXX.XXX.XXX:XXXX/secrettopic #URL of NTFY WITH leading HTTP and your secret topic at end
COPY gtfy.py /usr/bin
CMD ["python3", "/usr/bin/gtfy.py"]
```

Change ENV GOTIFY_HOST=, ENV GOTIFY_TOKEN=, and ENV NTFY_HOST= parameters.
Example

ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip3 install requests python-dotenv websocket-client
ENV GOTIFY_HOST=192.168.10.48:8181
ENV GOTIFY_TOKEN="CRpwR023ONqPR9D"
ENV NTFY_HOST=http://192.168.10.48:8180/mysupersecrettopic
COPY gtfy.py /usr/bin
CMD ["python3", "/usr/bin/gtfy.py"]


- Build Docker Image

```sh
docker build . -t="gtfy2ntfy"
```
- List the image
```sh
docker image ls
```
- Create and Test Container
```sh
docker run -d --name gtfy2ntfy gtfy2ntfy
docker ps
docker stop gtfy2ntfy
```

## Run the container forever (PREFERRED)
```sh
docker run -d --restart=always --name gtfy2ntfy gtfy2ntfy
```

- Other Commands in Docker
```sh
## List Hidden container if error exists
docker ps -a

## other commands
docker logs (containerID)
docker stop (containerID)
docker rm (containerid)
docker docker rmi (imageid)
docker image prune
docker builder prune --all -f
docker system prune --all
docker rm $(docker ps -all -q)
docker rmi $(docker image ls -q)
```

## Inspiration

Pushtify (Gotify to Pushover forwarder) - <https://github.com/sebw/pushtify>
NTFY - <https://docs.ntfy.sh/install/>
Gotify and iGotify - <https://github.com/androidseb25/iGotify-Notification-Assistent/tree/main>
Gotify-listener - <https://github.com/sanwebinfo/gtfy-listener>


## LICENSE

MIT
