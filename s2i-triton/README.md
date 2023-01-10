# s2i patch - triton model serving

This project consists of how to create a container with a model for serving on triton

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

Git folder structure:

```
models
└── [ model name ]
    └── 1 (version)
        └── model.savedmodel
            ├── saved_model.pb
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
  model-server

```

You can then run the resulting image via:

```
oc get pods
oc exec <pod> -- curl localhost:8000/v2/models/< model name >
```

## Links

- https://github.com/triton-inference-server/server
- https://github.com/openshift/source-to-image
- https://github.com/sclorg/container-common-scripts
