### UPDATE MACHINE 
echo 
echo "=============== Updating" 
sudo apt-get update -y 

#sudo chmod a+x /vagrant/argo.sh


### INSTALL KUBECTL 
echo 
echo "=============== Installing KUBECTL ===============" 
sudo curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" 
sudo curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256" 
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl 
sudo kubectl version --client --output=yaml 


### INSTALL KIND 
echo 
echo "=============== Installing KIND ===============" 
sudo curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64 
sudo chmod a+x ./kind 
sudo mv ./kind /usr/local/bin/kind 
sudo kind create cluster 
sudo kubectl cluster-info --context kind-kind 

### Wait for the kind-control-plane node to be ready 
sudo kubectl wait node --for=condition=Ready --timeout=60s kind-control-plane 
sudo kubectl get nodes 


### INSTALL ARGO WORKFLOW CLI 
echo 
echo "=============== Installing ARGO CLI ===============" 
sudo curl -LO https://github.com/argoproj/argo-workflows/releases/download/v3.4.5/argo-linux-amd64.gz 
sudo gunzip argo-linux-amd64.gz 
sudo chmod +x argo-linux-amd64 
sudo mv ./argo-linux-amd64 /usr/local/bin/argo 
sudo argo version 


### INSTALL ARGO WORKFLOW 
### Create Argo namespace 
sudo kubectl create namespace argo 
sudo kubectl get namespace 

### Install Latest Version of Argo 
sudo kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v3.4.5/install.yaml 

echo 
echo "=============== Waiting for the deployments to be created ===============" 
sudo kubectl -n argo wait --for=condition=available --timeout=90s --all deployment 

### Check Argo Deployments 
sudo kubectl get all -n argo 
sudo kubectl patch deployment argo-server --namespace argo --type='json' -p='[{"op": "replace", "path": "/spec/template/spec/containers/0/args", "value": [ "server", "--auth-mode=server" ]}]' 

### -w option wait for the submit to complete 
sudo argo submit -n argo -w https://raw.githubusercontent.com/argoproj/argo-workflows/master/examples/hello-world.yaml 

echo 
echo "=============== Workflows list ===============" 
sudo argo list -n argo 

#sudo argo get -n argo @latest 

sudo argo logs -n argo @latest >> argo_install 

echo 
echo "=============== Running Argo Dashboard on background ===============" 
sudo kubectl -n argo port-forward --address 192.168.56.10 deployment/argo-server 2746:2746 &
# sudo sed -i '$ a sudo kubectl -n argo port-forward --address 192.168.56.10 deployment/argo-server 2746:2746 & \n' /home/vagrant/.profile
# sudo source /home/vagrant/.profile
### Browse https://192.168.56.10:2746 to see Argo dashboard