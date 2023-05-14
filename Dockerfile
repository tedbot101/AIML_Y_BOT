FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3 && apt-get install -y python3-pip

RUN python3 -m pip install Flask==2.0.3
RUN python3 -m pip install --no-cache-dir programy


RUN mkdir /chatbot
ADD . /chatbot
WORKDIR /chatbot



# RUN mkdir chatbot
# RUN cd chatbot
# RUN git clone https://github.com/tedbot101/AIML_Y_BOT.git

# RUN python custom_bot.py

# VOLUME /gluon
# WORKDIR /gluon
# RUN git checkout docker
# RUN cp -a docs/site-example/ site