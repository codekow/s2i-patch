# s2i patch - triton model serving

This project consists of how to create a container with a model for serving on triton

## Usage
```
To build it in Openshift, run:
oc new-app nvcr.io/nvidia/tritonserver:22.11-py3~codekow/s2i-patch.git --context-dir=s2i-triton

To use it in Openshift, run:
oc new-app s2i-tritonserver:latest~codekow/ml-models.git --context-dir=models

You can then run the resulting image via:
oc get pods
oc exec <pod> -- curl localhost:8000/v2/models/< model name >
```