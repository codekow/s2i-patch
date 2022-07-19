# Introduction - Source to Image (s2i)

Source to image (s2i) is a simple method of containerizing code on the OpenShift platform (but can be used anywhere). The s2i process is lightweight, minimalistic, and barebones.

This quick, paved path, allows you to put an application into a container with basic requirements to run your code. In short, s2i means...

*YOU DON'T HAVE TO KNOW MUCH ABOUT CONTAINERS!*

 Follow the links at the bottom to learn more.

# Patch the s2i build?

Patching s2i images allow adding dependencies that are not default - dependencies that do not exist in the default s2i container.

## Why patch the Python s2i build?

Patch the s2i image if your app needs other dependencies.

Examples include:
  - Gurobi client libraries
  - Database connection drivers
  - Proxy ENV settings

Available patch build config templates are stored in the [openshift](openshift) folder in this repo.

# Patch s2i via `Dockerfile`

#TheHardWay

Use a `Dockerfile` when you NEED `root` for commands.

From a high level...
- Deploy code using the default s2i process
- Add templates from this repo into an OpenShift project (namespace)
- Click some buttons to layer / combine those templates into a new image
- Change your existing build from step #1 to build from the patched s2i image that you created in step #3
- Rejoice!!!

## Quickstart Command
The following command will create a build config to patch a base s2i image

```
# add odbc driver to python s2i image
oc process -f openshift/build-s2i-ms-odbc-17.yml | oc apply -f-
```

# Customize s2i via `assemble`

#TheEasierWay

Use `assemble` when you DO NOT need `root` for commands.

This allows you to customize your container via whatever scripting method you prefer (by default it is bash).

Move the mess of `ENTRYPOINT` scripts and `Dockerfile` (non root) `RUN` lines to `.s2i/bin/assemble`.

Move those `ENV` lines to `.s2i/environment`.

See [.s2i/bin/assemble](.s2i/bin/assemble)

# Links
- [OpenShift Docs - Source to Image](https://docs.openshift.com/container-platform/4.10/openshift_images/using_images/using-s21-images.html)
- [GitHub - Source to Image](https://github.com/openshift/source-to-image)
- [Python s2i Docs](https://docs.openshift.com/container-platform/3.11/using_images/s2i_images/python.html#using-images-python-configuration)