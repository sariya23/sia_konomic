# Run: docker run --network="host" --rm -it --entrypoint bash ci_cd_tests

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
ENV CHROMEDRIVER_VERSION 120.0.6099.109

# Download and install Chromedriver
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$CHROMEDRIVER_VERSION/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip
RUN mv chromedriver-linux64/chromedriver /usr/bin
RUN chmod +x /usr/bin/chromedriver

CMD ["pytest", "-n", "auto"]

