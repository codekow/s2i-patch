# S2I build types

## Local Build Type: Docker

```
podman build ./docker -t gradio
```

## Local Build Type: source (python)

```
# workaround for s2i w/ podman
mkdir -p ../scratch

s2i build \
  --as-dockerfile ../scratch/Dockerfile \
  . \
  registry.access.redhat.com/ubi8/python-38 \
  s2i-gradio

cd ../scratch
podman build -t gradio:s2i .

podman run \
  --rm -p 8080:8080 \
  localhost/gradio:s2i
```

## Deploy Gradio on OpenShift
```
NAMESPACE=model-serving
APP_NAME=model-client
APP_LABEL="app.kubernetes.io/part-of=${APP_NAME}"
BUILD_STRATEGY=docker

# alt: source build
# BUILD_STRATEGY=source

# update to model endpoint
INFERENCE_ENDPOINT=http://model-server-embedded:8000/v2/models/fingerprint

# s2i build
oc new-app \
  -n ${NAMESPACE} \
  --name=${APP_NAME} \
  -l ${APP_LABEL} \
  --env=INFERENCE_ENDPOINT=${INFERENCE_ENDPOINT} \
  --context-dir=/serving/client \
  --strategy=${BUILD_STRATEGY} \
  https://github.com/redhat-na-ssa/demo-rosa-sagemaker.git


# create external route
oc expose service \
  -n ${NAMESPACE} \
  ${APP_NAME} \
  -l ${APP_LABEL} \
  --port 8080 \
  --overrides='{"spec":{"tls":{"termination":"edge"}}}'
```
