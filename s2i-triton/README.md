# s2i patch - triton model serving

This project consists of how to create a container with a model for serving on triton

## Usage

Build s2i image in Openshift, run:

```
# use template
oc process -f openshift/build-s2i-triton.yml | oc apply -f-
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


```
oc new-app s2i-triton:latest~https://github.com/codekow/ml-models.git --context-dir=models
```

Build an image with a model via s2i (w/ git repo):

```
oc new-app s2i-triton:latest~https://github.com/codekow/ml-models.git --context-dir=models
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
