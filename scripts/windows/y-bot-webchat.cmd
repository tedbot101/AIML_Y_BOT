@echo off

cls
python -m programy.clients.restful.flask.webchat.client --config ..\..\config\windows\config.webchat.yaml --cformat yaml --logging ..\..\config\windows\logging.yaml
:end 

