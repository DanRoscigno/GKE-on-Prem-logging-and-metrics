# GKE-on-Prem-logging-and-metrics

### Grab the configuration
`git clone https://github.com/DanRoscigno/GKE-on-Prem-logging-and-metrics.git`
or
Click the *Clone or Download* button at the top right of https://github.com/DanRoscigno/GKE-on-Prem-logging-and-metrics

All of the rest of the commands will be run from the directory `GKE-on-Prem-logging-and-metrics`

### Set the cluster-admin-binding
Logging and metrics tools like Filebeat, Fluentd, Metricbeat, Prometheus, etc. run as DameonSets.  To deploy DaemonSets you need the cluster role binding `cluster-admin-binding`.  Create it now:

`kubectl create clusterrolebinding cluster-admin-binding  --clusterrole=cluster-admin --user=<the email address associated with your GKE account>`

### Deploy example application
This uses the Guestbook app from the Kubernetes docs.  The YAML has been concatenated into a single manifest, and Apache HTTP mod Status has been enabled for metrics gathering.

`kubectl create -f guestbook.yaml`

### Create secrets
Rather than putting the Elasticsearch and Kibana endpoints into the manifest files they are provided to the Filebeat pods as k8s secrets.  Edit the files `elasticsearch-hosts-ports` and `kibana-host-port` and then create the secret:

`kubectl create secret generic elastic-stack --from-file=./elasticsearch-hosts-ports --from-file=./kibana-host-port --namespace=kube-system`

### Deploy index patterns, visualizations, dashboards, and machine learning jobs
Filebeat and Metricbeat provide the configuration for things like web servers, caches, proxies, operating systems, container environments, databases, etc.  These are referred to as *Beats modules*.  By deploying these configurations you will be populating Elasticsearch and Kibana with visualizations, dashboards, machine learning jobs, etc.  

`kubectl create -f filebeat-setup.yaml`
`kubectl create -f metricbeat-setup.yaml`
#### Note: Depending on your k8s Node configuration, you may not need to deploy Jounalbeat.  If your Nodes use journald for logging, then deploy Journalbeat, otherwise Filebeat will get the logs
`kubectl create -f jojurnalbeat-setup.yaml`

### Deploy the Beat DaemonSets
`kubectl create -f filebeat-kubernetes.yaml`
`kubectl create -f metricbeat-kubernetes.yaml`
#### Same caveta as above, you may not need Journalbeat
`kubectl create -f journalbeat-kubernetes.yaml`

### Verify
`kubectl get pods -n kube-system`

Verify that the filebeat-setup pod completes
Verify that there is one filebeat pod per k8s Node running
Check the logs for the setup pod and one of the DaemonSet filebeat pods to ensure that they connected to Elasticsearch and Kibana (the setup pod connects to both)
