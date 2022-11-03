<h1 align="center">Welcome to z4k-license-calculator 👋</h1>
<p>
</p>

> A license calculator for Zerto for Kubernetes as a Service

## What does it do

This project produces a report of k8s nodes that are compatible with Z4k and also totals up the number of vCPUs so that licensing can be properly calculated

```sh
justin@cplane1:~$ kubectl get nodes -o json | curl -H "Content-Type: application/json" -X POST --data-binary @- http://10.10.1.157:8822/nodeinfo
```
Will return;
```json
{
    "status":"SUCCESS",
    "nodeData":[{
        "name":"node2",
        "vcpu":"4",
        "arch":"amd64",
        "osImage":"Ubuntu 22.04.1 LTS",
        "containerRuntime":"containerd://1.6.8",
        "kernelVersion":"5.15.0-52-generic",
        "kubeProxyVersion":"v1.25.3",
        "kubeletVersion":"v1.25.3"
    },{
        "name":"node2",
        "vcpu":"4",
        "arch":"amd64",
        "osImage":"Ubuntu 22.04.1 LTS",
        "containerRuntime":"containerd://1.6.8",
        "kernelVersion":"5.15.0-52-generic",
        "kubeProxyVersion":"v1.25.3",
        "kubeletVersion":"v1.25.3"
    }],
    "totalVcpus":8
}
```

## Install

```sh
docker-compose build
```

## Usage

Server:

```sh
docker-compose up -d
```

Client:
kubectl get nodes -o json | curl -H "Content-Type: application/json" -X POST --data-binary @- http://10.10.1.157:8822/nodeinfo

## Show your support

Give a ⭐️ if this project helped you!