# Big-Data-Processing-Toolbox
## Link to video demo and code walkthrough: 14848_demo video
https://www.youtube.com/channel/UCLd6VMGLnjg_cTwzjIvN4gg

## Step 0: Find Suitable Docker Images
- Apache Spark: https://hub.docker.com/r/bitnami/spark 
- Jupyter Notebook: https://hub.docker.com/r/jupyter/base-notebook
- SonarQube and SonarScanner: https://hub.docker.com/_/sonarqube?tab=description&page=3
- Apache Hadoop: 
master node: https://hub.docker.com/r/jupyter/base-notebook  
data node: https://hub.docker.com/r/bde2020/hadoop-datanode/tags  

## Step 1: Create all docker images and containers, and test it locally.
### 1. Apache Spark
- Docker image: https://hub.docker.com/r/bitnami/spark
- Command: `docker pull bitnami/spark`
         `docker run -p 8080:8080 bitnami/spark`
- Test this image by opening localhost:8080, you will see: 
![image](https://user-images.githubusercontent.com/89753601/142845071-69034d77-3f12-4979-9ef4-c4751012f18f.png)
### 2. Jupyter Notebook
- Docker image: https://hub.docker.com/r/jupyter/base-notebook
- Command: `docker pull jupyter/base-notebook`
         `docker run -p 8888:8888 jupyter/base-notebook`
- Command shows ![image](https://user-images.githubusercontent.com/89753601/142847107-4668acac-c95d-49f9-a5b0-6316b74c1a69.png)
- Test this image by opening http://127.0.0.1:8888/?token=50f45d73366b5773d34243b1747531c3c4f75b7e4678b121, you will see:
![image](https://user-images.githubusercontent.com/89753601/142847170-a946c55a-c9ba-4127-bbbc-5f6169edfa73.png)
### 3. SonarQube and SonarScanner
- SonarQube docker image: https://hub.docker.com/_/sonarqube?tab=description&page=3
- Command:`docker pull --platform linux/amd64 sonarqube:lts-community`
        `docker run --platform linux/amd64 -p 9000:9000 sonarqube:lts-community `
- No matching manifest for linux/arm64/v8 at first due to Mac M1 chip, so I add `--platform linux/amd64`. Then it works
![image](https://user-images.githubusercontent.com/89753601/142848762-7b97c9e6-fd22-43ec-b3f8-229eb6aa27f9.png)

### 4. Apache Hadoop
- Docker image for master node: https://hub.docker.com/r/jupyter/base-notebook
- Command: `docker pull --platform linux/amd64 bde2020/hadoop-namenode:latest`
           `docker run --platform linux/amd64 bde2020/hadoop-namenode:latest `
![image](https://user-images.githubusercontent.com/89753601/142857301-27522e4e-6ce8-47ac-a0db-6af5ac841135.png)
- Docker image for data node: https://hub.docker.com/r/bde2020/hadoop-datanode/tags
- Command: `docker pull --platform linux/amd64 bde2020/hadoop-datanode:latest`
           `docker run --platform linux/amd64 bde2020/hadoop-datanode:latest`
 ![image](https://user-images.githubusercontent.com/89753601/142858766-5c0b7d44-a12a-48b5-859c-bf54b490f7d3.png)
 
### 5. Terminal Application
- Docker image:
- Command: 
 
 
 ## Step 2: Cluster Intial Setup
 ![image](https://user-images.githubusercontent.com/89753601/143787874-cbf51760-f255-42e5-a1e9-bd92275a9fce.png)

 ## Step 3: Deploy Apache Spark and Jupyter Notebook
 - deployment:
 `docker pull bitnami/spark`
 `docker tag bitnami/spark gcr.io/big-data-processing-tool-box/bitnami/spark`
 `docker push gcr.io/big-data-processing-tool-box/bitnami/spark`
 - create service, expose, and set IP port 8080:8080
 ![image](https://user-images.githubusercontent.com/89753601/143789031-c6c55b79-d378-40a8-bd79-6f8e8e96b1e0.png)
![image](https://user-images.githubusercontent.com/89753601/143791382-e1991a7f-f5dc-490f-a3d8-521b1e81110a.png)

 - deployment:
 `docker pull jupyter/base-notebook`
 `docker tag jupyter/base-notebook gcr.io/big-data-processing-tool-box/jupyter/base-notebook`
 `docker push gcr.io/big-data-processing-tool-box/jupyter/base-notebook`
 - create service, expose, and set IP port 8888:8888
 ![image](https://user-images.githubusercontent.com/89753601/143789133-427f9acb-a1e6-483c-a910-acdf83d998fb.png)
![image](https://user-images.githubusercontent.com/89753601/143791390-70003fac-5209-4d76-a768-d28323944d20.png)
 
 ## Step 4: Deploy Hadoop and Sonar Scanner
 
 
 
 
 
 

       



