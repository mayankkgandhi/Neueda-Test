# Neueda Challenge

## TASK

- Write a python script, which will convert json files to xml files, encrypt and transfer it in a remote location.
- Pipeline:
    Json -> XML -> encryption -> transfer -> decryption -> XML
- Any given Json putted to container A appears in XML form on container B using mentioned pipeline.

## Solution

Solution is prepared as two Docker images, container_a to send files, and container_b to receive them.
Deployment of these containers is automated using shell script.

[Solution - Video Link](https://drive.google.com/file/d/1GZ-YvXdgFYuH1SMQv39Uj7XfyuLqRFI1/view?usp=sharing)

The container_a directory is responsible for,

- reading json files from `/jsons`
- converting json to xml
- encrypting xml
- pushing encrypted xml to rabbitmq queue over the network.

The container_b directory is responsible for,

- receiving encrypted data from rabbitmq queue
- decrypting the data back to xml
- store it in xml file at location `/xmls`

## Steps to Run

1. The script will build container images, create bridge network and run rabbitmq container.

```bash
sudo ./setup.sh
```

2. Run and execute the built images. The script will first execute the containerA_main container and then will execute the containerB_main container. The received files are stored in xmls directory.
  
```bash
sudo ./execute.sh
```

3. The script will cleanup all conatiner, it's images and network.

```bash
sudo ./cleanup.sh
```
