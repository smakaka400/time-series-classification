#!/bin/bash
set -e

echo "=========TRAINING AND SAVING MODEL========="
python sEMG_model.py

echo "=========TESTING MODEL APP========="
python model_deployment_tests.py

echo "=========BUILDING DOCKER IMAGE========="
docker build -t semg-app:latest .


# EDIT TAGS TO PUSH TO YOUR OWN DOCKERHUB LOCATION
echo "=========RETAGGING IMAGE========="
docker tag semg-app:latest steveyn400/semg-app:latest

echo "=========PUSHING IMAGE TO REGISTRY========="
docker push steveyn400/semg-app:latest


echo "=========CREATING KUBERNETES DEPLOYMENT========="
kubectl apply -f kubernetes_deployment.yaml

echo "=========EXPOSING KUBERNETES DEPLOYMENT WITH EXTERNAL IP ADDRESS========="
kubectl expose deployment semg-deployment --type=LoadBalancer --port=5000

echo "=========WAITING FOR DEPLOYMENT TO BE READY========="
sleep 30

echo "=========SUBMITTING EXAMPLE CURL REQUEST TO EXPOSED ENDPOINT========="
external_address=$(kubectl get services semg-deployment --output jsonpath='{.status.loadBalancer.ingress[0].ip}')
curl -X POST -F file=@test_predictions_correct.csv http://$external_address:5000/predict
