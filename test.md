## To access your Kubernetes service in **Chrome** and get the **IP of the server**, follow these steps:
---

# Step 1 :Get Service Details
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

 

