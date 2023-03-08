# Time Series Classification
This repo contains code to create a time series classification model using [pyts](https://pyts.readthedocs.io/en/latest/generated/pyts.classification.TimeSeriesForest.html) and deploy in a Kubernetes cluster.

## Deployment instructions
In order to create and deploy the model locally the following is required:
- Python (Python 3.7.12 was used), pandas==1.3.4, scikit-learn==1.0.1, joblib==1.1.0, pyts==0.12.0, Flask==2.2.3
- Docker
- Kubectl
- Minikube

First create a local Kubernetes cluster with Minikube, by running `minikube start` and then `minikube tunnel`. In a separate terminal, make the bash script executable with the command `chmod u+x deployment_script.sh`. Open `deployment_script.sh` and change the docker tags to your own repository. Then run `./deployment_script.sh` to train and save the model, run unit tests on the Flask app, create a Docker image serving the model, and deploy this image in your local Kubernetes cluster.

