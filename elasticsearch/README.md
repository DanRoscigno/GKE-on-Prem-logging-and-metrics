```
lsblk 
sudo mkdir /usr/share/elasticsearch
sudo mkfs.ext4 -m 0 -F -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb
sudo blkid /dev/sdb
sudo vi /etc/fstab
```

Add a line using the output of `blkid` to the fstab like so:
```
UUID="UUID from blkid command" /usr/share/elasticsearch ext4 discard,defaults,nofail 0 2
```
and continue

```
sudo reboot
```

Reconnect

```
df -h
sudo yum install -y wget
sudo yum install -y java-1.8.0-openjdk.x86_64
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.6.1.rpm
sudo rpm -i elasticsearch-6.6.1.rpm
sudo chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/
sudo vi /etc/elasticsearch/elasticsearch.yml
```

Use the files from this dir as a guide to creating your `elasticsearch.yml` files, change the hostnames.

```
sudo  /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-geoip
sudo  /usr/share/elasticsearch/bin/elasticsearch-plugin install ingest-user-agent
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service
sudo reboot
```

Reconnect

```
netstat -an | grep 9200
curl `hostname`:9200/_cluster/health?pretty=true
```

### Install Kibana
On one system do this:

```
wget https://artifacts.elastic.co/downloads/kibana/kibana-6.6.1-x86_64.rpm
sudo rpm -i kibana-6.6.1-x86_64.rpm 
sudo vi /etc/kibana/kibana.yml 
```
Use the contents of `kibana.yml` from this directory as a guide, specify the hostnames of your Elasticsearch nodes.

```
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable kibana.service
sudo systemctl start kibana.service
netstat -an | grep 5601
sudo systemctl status kibana.service
curl `hostname`:5601/api/status
```
