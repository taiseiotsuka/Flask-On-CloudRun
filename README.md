# Flask-On-CloudRun

This project uses [Cloud Run](https://cloud.google.com/run/) and [Cloud Firestore](https://firebase.google.com/docs/firestore).

You need to create actor collection in Cloud Firestore beforehand.

## Python version

3.6.x

## Local settings

```
## bash

export FLASK_DEBUG=1

## Next is skip OK
export GOOGLE_APPLICATION_CREDENTIALS='path'
```

## Make command

```
make build ... create docker image. 

make run ... start flask container.

make tag ... Google Container Registry Name for push.

make push  ... Push to Google Container Registry.

```

## Edit file

### make file

```
## skip OK

PROJECT = project_id
REGION = region_host
```

### develop config file

```
mkdir -p instance/config/
cp example.cfg instance/config/dev.cfg
```

## Ready?

```
git clone https://github.com/taiseiotsuka/Flask-On-CloudRun.git
cd Flask-On-CloudRun
make build

## Local settings ...

make run

curl http://127.0.0.1:5000/example/hello
'Hello World!!'
```
