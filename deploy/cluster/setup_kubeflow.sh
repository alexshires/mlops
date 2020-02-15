# create namespace
kubectl create namespace kubeflow
# apply label
kubectl label namespace kubeflow serving.kubeflow.org/inferenceservice=enabled