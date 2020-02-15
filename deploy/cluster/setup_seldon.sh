#!/usr/bin/env bash
kubectl create namespace seldon
kubectl config set-context $(kubectl config current-context) --namespace=seldon
kubectl create namespace seldon-system
# install istio
helm install seldon-core seldon-core-operator --repo https://storage.googleapis.com/seldon-charts --set istio.enabled=true --set usageMetrics.enabled=true --namespace seldon-system
# check services
kubectl rollout status deploy/seldon-controller-manager -n seldon-system