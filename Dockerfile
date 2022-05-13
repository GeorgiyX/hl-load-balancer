FROM ubuntu:20.04

RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y python3-venv

WORKDIR /app
COPY requirements.txt .
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt

COPY wsgi.py .
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
EXPOSE 5000
