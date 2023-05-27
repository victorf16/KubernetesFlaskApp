# projetoKubernets

# Comandos efetuados no docker para gerar imagem
# importante estar logado no docker hup para realizar o push

# utilizamos o source code que criamos no link https://github.com/victorf16/KubernetesFlaskApp

docker build -t victorf16/fidelizamaisvoce .
docker run -d -p 80:5000 --name fidelizamaisvoce  victorf16/fidelizamaisvoce 
docker push victorf16/fidelizamaisvoce 


# comandos que utilizamos no kubernets 
# Logar no kubernets
az account set --subscription 9359d480-32ba-4a9d-bb0e-3f1ea099e8f0

az aks get-credentials --resource-group kubernetes --name aks-trabalho