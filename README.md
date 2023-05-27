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

### Sertifique se que os arquivos abaixo foram baixados no repositorio.
### Então execute os seguintes comandos kubectl create -f deployment.yml e o comando kubectl create -f service.yml  
![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/748fbad3-9aa7-4893-8133-a9355f1a8509)

### cetifique se com os comandos kubectl get deployments -A e kubectl get svc -A se o fidelizamaisvoce-deployment e o fidelizamaisvoce-deployment-service foram criados respectivamente.
![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/77ec542d-d281-406e-940a-e246a256abef)



