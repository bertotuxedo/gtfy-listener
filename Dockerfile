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
