# Big-Data-Processing-Toolbox
## Link to video demo and code walkthrough: 14848_demo video
https://www.youtube.com/channel/UCLd6VMGLnjg_cTwzjIvN4gg

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

- SonarScanner docker image:

### 4. Apache Hadoop
- Docker image for master node: https://hub.docker.com/r/jupyter/base-notebook
- Command: `docker pull --platform linux/amd64 bde2020/hadoop-namenode:latest`
           `docker run --platform linux/amd64 bde2020/hadoop-namenode:latest `
![image](https://user-images.githubusercontent.com/89753601/142857301-27522e4e-6ce8-47ac-a0db-6af5ac841135.png)
- Docker image for data node: https://hub.docker.com/r/bde2020/hadoop-datanode/tags
- Command: `docker pull --platform linux/amd64 bde2020/hadoop-datanode:latest`
           `docker run --platform linux/amd64 bde2020/hadoop-datanode:latest`
 ![image](https://user-images.githubusercontent.com/89753601/142858766-5c0b7d44-a12a-48b5-859c-bf54b490f7d3.png)
 
 

       



