## To access your Kubernetes service in **Chrome** and get the **IP of the server**, follow these steps:
---

# Step 1 :Get Service Details
run
```
kubectl get svc
```

example output
 
### **Alternative Approach with Markdown Table & HTML Styling:**
GitHub does not support direct **coloring inside code blocks**, so for an **exact match** with yellow highlighting, you can use **HTML inside Markdown**:

```markdown
<table>
  <tr>
    <th>NAME</th>
    <th>TYPE</th>
    <th>CLUSTER-IP</th>
    <th>EXTERNAL-IP</th>
    <th>PORT(S)</th>
  </tr>
  <tr>
    <td>airflow-webserver</td>
    <td>LoadBalancer</td>
    <td><code style="color: #d4af37;">10.100.200.10</code></td>
    <td><code style="color: #d4af37;">34.120.45.67</code></td>
    <td><code style="color: #d4af37;">8080:80/TCP</code></td>
  </tr>
  <tr>
    <td>postgres-postgresql</td>
    <td>ClusterIP</td>
    <td><code style="color: #d4af37;">10.100.200.11</code></td>
    <td>&lt;none&gt;</td>
    <td><code style="color: #d4af37;">5432/TCP</code></td>
  </tr>
</table>

