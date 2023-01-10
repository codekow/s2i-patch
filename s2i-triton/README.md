# s2i patch - triton model serving

This project consists of how to create a container with a model for serving on triton

## Folder Info

Triton model folder structure:

```
[ model name ]
    └── 1 (version)
        └── model.savedmodel
            ├── saved_model.pb
```

## Usage

Build s2i image in Openshift, run:

```
oc new-build \
  https://github.com/codekow/s2i-patch.git \
  --name s2i-triton \
  --context-dir /s2i-triton
  --strategy docker
```

Build an image with a model via s2i (w/ git repo):

```
oc new-app \
  s2i-triton:latest~https://github.com/codekow/s2i-patch.git \
  --name example-triton-server \
  --strategy source \
  --context-dir=/s2i-triton/models
```

Build a model serving image via local folder:

```
# configure new build config
oc new-build \
  --image-stream s2i-triton:latest \
  --name model-server \
  --strategy source \
  --binary \
  --context-dir .

# start build from local folder
oc start-build \
  model-server \
  --from-dir models

# deploy app from model image
oc new-app \
  model-server \
  --allow-missing-imagestream-tags

# expose api via (tls) route
oc expose service model-server \
  --port 8000 \
  --overrides='{"spec":{"tls":{"termination":"edge"}}}'
```



Test the model server

```
# test via route
HOST=$(oc get route model-server --template={{.spec.host}})

curl -s https://${HOST}/v2 | python -m json.tool

curl -s https://${HOST}/v2/models/< model name > | python -m json.tool


# test via localhost
oc get pods
oc exec deploy/model-server -- curl -s localhost:8000/v2
oc exec deploy/model-server -- curl -s localhost:8000/v2/models/< model name >
```

Expose metrics (optional)

```
oc expose service model-server \
  --name model-server-metrics \
  --port 8002 \
  --overrides='{"spec":{"tls":{"termination":"edge"}}}'
```

You can then run the resulting image via:


## Links

- https://github.com/triton-inference-server/server
- https://github.com/openshift/source-to-image
- https://github.com/sclorg/container-common-scripts
