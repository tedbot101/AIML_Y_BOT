@echo off

cls


python -m programy.clients.restful.flask.client --config ..\..\config\windows\config.yaml --cformat yaml --logging ..\..\config\windows\logging.yaml
goto end


:end  

