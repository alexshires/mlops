# mlops
MLOps demo 2020

Based on: https://databricks.com/session/how-to-utilize-mlflow-and-kubernetes-to-build-an-enterprise-ml-platform 

# Key technologies

* Model training: mlfow
* Model packaging: Docker
* Model registry: mlflow
* Deployment: Kubernetes
* Model serving: Seldon-core
* Pipeline: Kafka
* Producer/Consumer: Python
* Testframework: PyTest

# Process:

* Train a set of basic models (iris?)
* Package and config in registry
* Set up serving environment
    * K8s for containers
    * Kafka producer / consumer chain
    * Seldon-core for deployments
    * anything else?
* Deploy model (framework?)
* Run test script
