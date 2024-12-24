# GTFY 🚀

[![docker-image](https://github.com/sanwebinfo/gtfy-listener/actions/workflows/docker.yml/badge.svg)](https://github.com/sanwebinfo/gtfy-listener/actions/workflows/docker.yml)  

Gotify to `Ntfy.sh` forwarder. This includes a few corrections and focuses on a http connection on a homeserver. This works from my Proxmox Server to Gotify to NTFY.

Forward Gotify Push Messages 🚀 to `Ntfy.sh` Push server by using websocket 🛸

using Gotify stream to Listen the Gotify Push Notifications via websocket Connection and Froward it to Ntfy Push server.

## Setup

```sh
git clone https://github.com/bertotuxedo/gtfy-listener
cd gtfy-listener

## local test
## install packages
pip install -r requirements.txt
touch .env
```

- Env File `.env`

```sh
NTFY = "<NTFY Push server URL without HTTP(S)>" 
GOTIFY_HOST = "<http://Gotify host URL:Port/secrettopic>"
GOTIFY_TOKEN = "<GOTIFY CLIENT TOKEN>"

## test
python3 gtfy.py

```

## Docker 🐬

Keep Running the Python Script in Docker  

- Update the `.dockerfile` before build - Replace example `ENV` with yours  

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

- Run docker compose

```sh
## Start docker
docker compose up -d
```

- Other docker Commands
```sh

## Build image
docker build . -t="gtfy-listener"

## List the image
docker image ls

## Create and Test Container
docker run -d --name gtfy gtfy-listener
docker container ps
docker stop (containerID)

## Run the container forever
docker run -d --restart=always --name gtfy gtfy-listener

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

## LICENSE

MIT
