# GKE-on-Prem-logging-and-metrics

### Set the cluster-admin-binding
Logging and metrics tools like Filebeat, Fluentd, Metricbeat, Prometheus, etc. run as DameonSets.  To deploy DaemonSets you need the cluster role binding `cluster-admin-binding`.  Create it now:

`kubectl create clusterrolebinding cluster-admin-binding  --clusterrole=cluster-admin --user=<the email address associated with your GKE account>`

### Create secrets
`kubectl create secret generic elastic-stack --from-file=./elasticsearch-hosts-ports --from-file=./kibana-host-port --namespace=kube-system`

### Deploy index patterns, visualizations, dashboards, and machine learning jobs
`kubectl create -f filebeat-setup.yaml`

### Deploy the Filebeat DaemonSet
`kubectl create -f filebeat-kubernetes.yaml`

### Verify
`kubectl get pods -n kube-system`

Verify that the filebeat-setup pod completes
Verify that there is one filebeat pod per k8s Node running
Check the logs for the setup pod and one of the DaemonSet filebeat pods to ensure that they connected to Elasticsearch and Kibana (the setup pod connects to both)
