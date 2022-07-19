# s2i patch - add gurobi

Gurobi Optimizer is a commercial optimization solver created by Gurobi. There is a python interface for Gurobi called gurobipy that is currently only found in the anaconda dependency repos. In order to reduce the footprint of the container we opted not to download and install anaconda in a container and opted to install it according to docs outside of anaconda.

## Build Information

The Python Gurobi image is currently built on top of the [python s2i image](https://docs.openshift.com/container-platform/3.11/using_images/s2i_images/python.html#overview). 

You can find how to build this base image in your project/namespace [here](). With this repo you can use the [Docker Build Template]() or the openshift build template provided in the repo.

## How To Build your Application with this Image

Because this image was built on top of the python s2i image you can use the source build image strategy in openshift to build your image. The same variables that are being used for the python s2i image will also work and operate the same way in the python-gurobi image.

You can find more information about the python s2i image [here](https://docs.openshift.com/container-platform/3.11/using_images/s2i_images/python.html#using-images-python-configuration).

## Additional Note

You will also need to add environemnt variables for your pod to use XOM's HTTP proxy, so that your code can access the Gurobi server which lives in XOM's Azure. Add these environment variables to your deployment config:

```
https_proxy: http://hoeprx01.na.xom.com:8080
https_proxy: http://hoeprx01.na.xom.com:8080
no_proxy: .xom.com,localhost,.localdomain.com,ticket,nexus,nexus.na.xom.com,pricesweb
```

## How to Login to Gurobi Server
```bash
grbcluster login --manager https://hostname.domain --username=userid
```

## Python Example of How to Execute against Gurobi Server

```python
import os
import gurobipy as gp

env = gp.Env(empty=True)
env.setParam(gp.GRB.Param.CSTLSInsecure, 0)
env.setParam(gp.GRB.Param.CSManager, 'https://gurobi.xomsvcs.com')
env.setParam(gp.GRB.Param.ServerPassword, os.getenv('GUROBI_SERVER_PASSWORD', 'pass'))
env.setParam(gp.GRB.Param.UserName, os.getenv('GUROBI_SERVER_USERNAME', 'gurobi'))
env.start()

try:

    # Create a new model
    m = gp.Model("mip1", env=env)

    # Create variables
    x = m.addVar(vtype=gp.GRB.BINARY, name="x")
    y = m.addVar(vtype=gp.GRB.BINARY, name="y")
    z = m.addVar(vtype=gp.GRB.BINARY, name="z")

    # Set objective
    m.setObjective(x + y + 2 * z, gp.GRB.MAXIMIZE)

    # Add constraint: x + 2 y + 3 z <= 4
    m.addConstr(x + 2 * y + 3 * z <= 4, "c0")

    # Add constraint: x + y >= 1
    m.addConstr(x + y >= 1, "c1")

    # Optimize model
    m.optimize()

    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))

    print('Obj: %g' % m.objVal)

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')
```
## Connect Matlab to Gurobi Server
To Do