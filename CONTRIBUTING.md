# Contributing

### System requirements

Install these, some you should already have. At the time of writing, using the 
latest versions of these is preferred. 

 - [Docker](https://docs.docker.com/get-docker/) ->  Container runtime
 - [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) -> kubernetes CLI
 - [helm](https://helm.sh/docs/intro/install/) -> kubernetes deployment CLI
 - [minikube](https://minikube.sigs.k8s.io/docs/start/) -> micro kubernetes deployment
 - **Make sure CPU Virtualization is enabled on your system**! This is doable through the 
   BIOS if your CPU supports it. (most modern systems support it but needs to be 
   enabled)

## Local Development

To set up your development environment, read the following steps

### Create a Virtual Environment

#### Windows:
```shell
> py -3 -m venv venv
> venv\Scripts\activate
```

#### Linux:
```shell
$ python3 -m venv venv
$ . venv/bin/activate
```

From this point on, the ``Makefile`` can be used for convenience. However, it is important to make sure the
virtual environment is activated when running any ``make`` commands.

### Installing Requirements

To install required packages and setup git hooks, use
```shell
$ make setup
```

This command will also need to be rerun if the ``setup.py`` or ``setup.cfg`` files are modified.

### Running in a Development Environment

To launch the project with Docker and test it, use
```shell
$ make dev
```

### Running the Linter

The linter automatically runs pre-commit, but to run the linter at an arbitrary time, use
```shell
$ make lint
```

### Running Unit Tests

To run the unit tests, use
```shell
$ make test
```

### Running Tests with Coverage

To run the tests and generate a coverage report, use
```shell
$ make coverage
```

### Building Documentation

To build and show documentation, use:
```shell
$ make docs
```

### Cleaning Artifacts

To clean all artifacts from builds, docs, coverage, etc, use
```shell
$ make clean
```

## Deployment Development
   
### Initial Set up
Run these before you start developing. These will build your local cluster that 
mirrors prod and launches the infinity database.

 1. Pull the latest dev-ops charts from the infrastructure department. 
    *This will take minute or two initially.*
    ```shell
    make ops
    ```
 2. Launch infinity. You should specify the version you want to use.
    ```shell
    make infinity VERSION="{VERSION NUMBER}"
    ```
 3. **In a different shell** launch OpenFaaS. This will port forward the gateway 
    to your box and allow you to do function deployments. The generated username 
    and password will be in the output from this command.
    ```shell
    make openfaas
    ```
    * You can run `make openfaas-creds` to get the credentials after the fact.    

 4. **In original development shell** Point docker to the minikube cluster. **THIS IS VERY IMPORTANT!**
    ```shell
    eval $(minikube docker-env --shell='cmd|powershell|bash|zsh')
    ```

### Development Cycle
This is the iteration cycle. As you make changes, you will execute these 
commands to deploy your application to the cluster. **YES**, this does mean you have 
to rebuild the container each time, but the build process is not long.

 5. Deploy serenity. The version here is the deployment spec that dev ops has 
    created for serenity. **THIS IS NOT THE SAME VERSION AS THE REPOSITORY!**
    ```shell
    make serenity VERSION="{VERSION NUMBER}"
    ```
    a. If this hangs on `helm install --set "version=dev" serenity ./.ops/charts/serenity/0.1.0/ --wait`, 
    press `ctrl+c` and it will release the shell. Then run `make logs`. This will tell you why the 
    deployment failed. If that still is not enough information, run `kubectl describe deployments/serenity`. 
    Copy the output from both the kubectl and logs command into Discord and ask for help. 
 6. Open [http://localhost:3030/graphql](http://localhost:3030/graphql). This is 
    the serenity service running inside your cluster.
    
### Clean up

 7. Pause the cluster. You should do this because minikube will take up quite a bit of 
    compute power on your box. 
    ```shell
    minikube stop
    ```

### Devops updates

If there is an update to the dev op's deployment set up, ask for the new version 
number and run the following.

```shell
make ops
```

This will deplete the current deployment specs and update with the latest from infra.
Now all Infinity and Serenity version numbers will need to match the versions op's has 
given you.

### Troubleshoot

 * Windows errors with the following.
    ```shell
    * Failed to start docker container. Running "minikube delete" may fix it: creating host: create host timed out in 360.000000 seconds
    
    X Exiting due to DRV_CREATE_TIMEOUT: Failed to start host: creating host: create host timed out in 360.000000 seconds
    * Suggestion: Try 'minikube delete', and disable any conflicting VPN or firewall software
    * Related issue: https://github.com/kubernetes/minikube/issues/7072
    ```
    * Solution: Disable Windows Firewall Defender and reboot. You can then run `make ops` and 
      re-enable Windows Firewall Defender. 