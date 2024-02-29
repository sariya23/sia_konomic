# Run: docker run sia_konomic:2.0.0

FROM python:3.11
WORKDIR /app
COPY . .

RUN pip install -r requirements/docker_requirements.txt

# We need wget to set up the PPA and unzip to install the Chromedriver\
RUN apt install -y wget unzip

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt update && apt -y install google-chrome-stable

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 122.0.6261.57
ENV PYTHONPATH /app

# Download and install Chromedriver
RUN wget https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip
RUN mv chromedriver-linux64/chromedriver /usr/bin
RUN chmod +x /usr/bin/chromedriver


CMD ["pytest", "-n", "auto"]

