#tutorial #7: kubernetes

es un sistema de código libre para la 
automatización del despliegue, ajuste de escala y manejo de aplicaciones en contenedores1​ que fue originalmente diseñado por Google y donado a la Cloud Native Computing Foundation (parte de la Linux Foundation). Soporta diferentes entornos para la ejecución de contenedores, incluido Docker.

para instalarlo hacemo lo siguiente


```
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
```

luego habilitamos los permisos de ejecucion 

```
chmod +x ./kubectl
```

movemos el bin a PATH

luego hacemos
```
sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2 curl
```
```
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```

```
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
```

```
sudo apt-get update
```

```
sudo apt-get install -y kubectl
```

instalamos minikube para el primer ejercicio
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```

```
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

**MINIKUBE**

minikube es una herramineta de kubernetes que te permite correr la apliacion localmente 

creamos una carpeta minikube

dentro de ella hay 2 archivos


```
minikube start
```


**esperamos** 
nos deberia mostrar algo asi
ikube start
😄  minikube v1.16.0 en Ubuntu 16.04
✨  Automatically selected the docker driver
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
💾  Downloading Kubernetes v1.20.0 preload ...
    > preloaded-images-k8s-v8-v1....: 491.00 MiB / 491.00 MiB  100.00% 3.29 MiB
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparando Kubernetes v1.20.0 en Docker 20.10.0...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔎  Verifying Kubernetes components...
❗  Executing "docker container inspect minikube --format={{.State.Status}}" took an unusually long time: 5.554375473s
💡  Restarting the docker service may improve performance.
❗  Executing "docker container inspect minikube --format={{.State.Status}}" took an unusually long time: 5.557906699s
💡  Restarting the docker service may improve performance.
🌟  Enabled addons: default-storageclass, storage-provisioner
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default


**KUBECTL**
esto es una herramienta que te perminte hace comandos en los cluster

```
kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4
```

```
kubectl get deployments
```
nos debeira mostrar
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
hello-node   0/1     1            0           16s


```
kubectl get pods
```
NAME                          READY   STATUS    RESTARTS   AGE
hello-node-7567d9fdc9-t9l8s   1/1     Running   0          64s


```
kubectl get events
```
LAST SEEN   TYPE      REASON                    OBJECT                             MESSAGE
2m8s        Normal    Scheduled                 pod/hello-node-7567d9fdc9-t9l8s    Successfully assigned default/hello-node-7567d9fdc9-t9l8s to minikube
2m2s        Normal    Pulling                   pod/hello-node-7567d9fdc9-t9l8s    Pulling image "k8s.gcr.io/echoserver:1.4"
83s         Normal    Pulled                    pod/hello-node-7567d9fdc9-t9l8s    Successfully pulled image "k8s.gcr.io/echoserver:1.4" in 38.595520588s
81s         Normal    Created                   pod/hello-node-7567d9fdc9-t9l8s    Created container echoserver
79s         Normal    Started                   pod/hello-node-7567d9fdc9-t9l8s    Started container echoserver
2m8s        Normal    SuccessfulCreate          replicaset/hello-node-7567d9fdc9   Created pod: hello-node-7567d9fdc9-t9l8s
2m8s        Normal    ScalingReplicaSet         deployment/hello-node              Scaled up replica set hello-node-7567d9fdc9 to 1
4m54s       Normal    Starting                  node/minikube                      Starting kubelet.
4m53s       Normal    NodeHasSufficientMemory   node/minikube                      Node minikube status is now: NodeHasSufficientMemory
4m53s       Normal    NodeHasNoDiskPressure     node/minikube                      Node minikube status is now: NodeHasNoDiskPressure
4m53s       Normal    NodeHasSufficientPID      node/minikube                      Node minikube status is now: NodeHasSufficientPID
4m52s       Normal    NodeNotReady              node/minikube                      Node minikube status is now: NodeNotReady
4m50s       Normal    NodeAllocatableEnforced   node/minikube                      Updated Node Allocatable limit across pods
4m42s       Normal    NodeReady                 node/minikube                      Node minikube status is now: NodeReady
4m39s       Normal    RegisteredNode            node/minikube                      Node minikube event: Registered Node minikube in Controller
4m10s       Warning   readOnlySysFS             node/minikube                      CRI error: /sys is read-only: cannot modify conntrack limits, problems may arise later (If running Docker, see docker issue #24000)
4m10s       Normal    Starting                  node/minikube                      Starting kube-proxy.



```
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
```



```
kubectl get services
```
hello-node   LoadBalancer   10.105.62.156   <pending>     8080:32514/TCP   8s
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          6m6s



```
minikube service hello-node
```
❗  Executing "docker container inspect minikube --format={{.State.Status}}" took an unusually long time: 2.532260714s
💡  Restarting the docker service may improve performance.
|-----------|------------|-------------|---------------------------|
| NAMESPACE |    NAME    | TARGET PORT |            URL            |
|-----------|------------|-------------|---------------------------|
| default   | hello-node |        8080 | http://192.168.49.2:32514 |
|-----------|------------|-------------|---------------------------|
🎉  Opening service default/hello-node in default browser...





