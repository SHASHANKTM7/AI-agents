## To access your Kubernetes service in **Chrome** and get the **IP of the server**, follow these steps:
---

## Step 1 :Get Service Details
run
```
kubectl get svc
```

example output
``` scss
NAME                        TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
airflow-webserver           LoadBalancer   10.100.200.10   34.120.45.67    8080:80/TCP      10m
postgres-postgresql         ClusterIP      10.100.200.11   <none>          5432/TCP         10m
```

## Step 2: Check the Type of Service
- **If** `TYPE=LoadBalancer` → The **`EXTERNAL-IP`** (e.g., **`34.120.45.67`**) is the public IP. Open Chrome and visit:
  ```arduino
  http: *//34.120.45.67:8080*
  ```
- **If** `TYPE=ClusterIP` → This is only accessible inside the cluster. You need to use `port-forward` (see next step).
- If `TYPE=NodePort` → The service is exposed on a port (e.g.,`30080`). Run:
```
kubectl get nodes -o wide
```
Find the **EXTERNAL-IP** of the node and access it in Chrome:
```arduino
_http://<NODE-EXTERNAL-IP>:30080_
```
  

 

