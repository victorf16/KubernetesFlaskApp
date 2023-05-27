* projetoKubernets

* Comandos efetuados no docker para gerar imagem
* importante estar logado no docker hup para realizar o push

* utilizamos o source code que criamos no link https://github.com/victorf16/KubernetesFlaskApp

docker build -t victorf16/fidelizamaisvoce .
docker run -d -p 80:5000 --name fidelizamaisvoce  victorf16/fidelizamaisvoce 
docker push victorf16/fidelizamaisvoce 


* comandos que utilizamos no kubernets 
* Logar no kubernets
az account set --subscription 9359d480-32ba-4a9d-bb0e-3f1ea099e8f0

az aks get-credentials --resource-group kubernetes --name aks-trabalho

![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/e62ee118-afde-4f20-b03b-f1100f557cb6)
### Apos realizar o login digite o comando kubectl get deployments --all-namespaces=true, a saida desse comando deve ser parecida com a saida da imagem abaixo
![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/ce73f495-1f56-4b6e-b9b3-3a3a0f76a0ec)

### Clone o repositorio dentro do ambiente do azure powershell para clonar o repositorio onde esta o nosso projeto
![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/a95c984a-4a77-44d7-9fbd-c8c50961abd2)

### Abra o diretorio utilizando o comando cd


