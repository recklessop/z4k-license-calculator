# main.py

from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/nodeinfo")
async def nodeinfo(info : Request):
    req_info = await info.json()

    results = []
    vcpus = 0

    if 'items' in req_info:
        nodes = req_info['items']
        data = {}
        for node in nodes:
            if 'taints' in node['spec']:
                print("Taint exists, dont count this node")
            else:
                print("Node not tainted")
                data['name'] = node['metadata']['labels']['kubernetes.io/hostname']
                data['vcpu'] = node['status']['allocatable']['cpu']
                data['arch'] = node['status']['nodeInfo']['architecture']
                data['osImage'] = node['status']['nodeInfo']['osImage']
                data['containerRuntime'] = node['status']['nodeInfo']['containerRuntimeVersion']
                data['kernelVersion'] = node['status']['nodeInfo']['kernelVersion']
                data['kubeProxyVersion'] = node['status']['nodeInfo']['kubeProxyVersion']
                data['kubeletVersion'] = node['status']['nodeInfo']['kubeletVersion']
                results.append(data)
                vcpus = vcpus + int(data['vcpu'])
    
    return {
        "status" : "SUCCESS",
        "nodeData" : results,
        "totalVcpus" : vcpus
    }
