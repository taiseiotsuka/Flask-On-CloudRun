APP_NAME = flask
PROJECT = ***
REGION = ***
V = latest

build:
	docker build -t $(APP_NAME) .

run:
	docker run -p 5000:5000 --name $(APP_NAME) -itd $(APP_NAME)

tag:
	docker tag $(APP_NAME) $(REGION)/$(PROJECT)/$(APP_NAME):$(V)

push:
	docker push $(REGION)/$(PROJECT)/$(APP_NAME):$(V)