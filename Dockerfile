FROM ubuntu:18.04

RUN sudo apt-get update
RUN sudo apt-get install -y python3.7.4 && apt-get install -y git

RUN pyhon -m pip install Flask==2.1.0
RUN pyhon -mpip install --no-cache-dir programy

RUN mkdir chatbot
RUN cd chatbot
RUN git clone 

