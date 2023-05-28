## Acesso Azure

* Para realizar os passsos abaixo é necessário a conta da azure ativa, acessar https://portal.azure.com para acessar a azure, no nosso caso utilizamos a subscrição disponibilizada na nossa sala de aula do curso MBA em Engenharia DevOps FIAP 15DVP

Para executar este material deve estar com a versão mais recetne do azure CLI instalada, instruções e detalhes de como instalar o azure CLI no Link abaixo
https://learn.microsoft.com/pt-br/cli/azure/install-azure-cli-windows?tabs=azure-cli

## Instalação do Docker para criar o Build

Para executar este material deve estar com a versão mais recente Docker instalado, no nosso caso utilizamos o docker para Windows, instruções e detalhes de como instalar o Docker no link abaixo 

https://www.bing.com/search?q=como+isntalar+o+docker+no+windwos&cvid=f38061e9dcbb4a41905126129bb47951&aqs=edge..69i57j0l8.3607j0j4&FORM=ANAB01&PC=DCTS



### Clone o repositorio dentro do ambiente do azure powershell para clonar o repositorio onde esta o nosso projeto

Após a instalação do docker e do Azure CLI, 

![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/a95c984a-4a77-44d7-9fbd-c8c50961abd2)

## Build do docker

* projetoKubernets

* Comandos efetuados no docker para gerar imagem

* Certifique-se que para realziar o comando abaixo é necessário executar na paste em que se encontra o arquivo Dockerfile , apos realizar o git clone baste acessar utilizando o comando cd e o nome da pasta que foi gerada pelo comando git 

 cd ./KubernetesFlaskApp/

* estando na pasta basta executar os comandos abaixo (certifique de usar o seu resource group, no nosso caso utilizamos o resource group kubernetes e criamos o container register chamado mycontainerregistry15dvp lembre-se que este nome deve ser único diferente do nosso utilizado no trabalho)

az acr create --resource-group kubernetes   --name mycontainerregistry15dvp --sku Basic



<img width="495" alt="image" src="https://github.com/victorf16/KubernetesFlaskApp/assets/28166733/18962482-0f1e-41de-9d3c-568281e96df5">

az acr build --image victorf16/fidelizamaisvoce --registry mycontainerregistry15dvp  --file Dockerfile . 

docker build -t victorf16/fidelizamaisvoce .

docker run -d -p 80:5000 --name fidelizamaisvoce  victorf16/fidelizamaisvoce 

* importante estar logado no docker hup para realizar o push

docker push victorf16/fidelizamaisvoce 



* utilizamos o source code que criamos no link https://github.com/victorf16/KubernetesFlaskApp




## Azure AKS 
* Logar no kubernets
az account set --subscription 9359d480-32ba-4a9d-bb0e-3f1ea099e8f0

az aks get-credentials --resource-group kubernetes --name aks-trabalho

![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/e62ee118-afde-4f20-b03b-f1100f557cb6)
### Apos realizar o login digite o comando kubectl get deployments --all-namespaces=true, a saida desse comando deve ser parecida com a saida da imagem abaixo
![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/ce73f495-1f56-4b6e-b9b3-3a3a0f76a0ec)



### Abra o diretorio utilizando o comando cd

### Sertifique se que os arquivos abaixo foram baixados no repositorio.
### Então execute os seguintes comandos kubectl create -f deployment.yml e o comando kubectl create -f service.yml  
![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/748fbad3-9aa7-4893-8133-a9355f1a8509)

### cetifique se com os comandos kubectl get deployments -A e kubectl get svc -A se o fidelizamaisvoce-deployment e o fidelizamaisvoce-deployment-service foram criados respectivamente.
![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/77ec542d-d281-406e-940a-e246a256abef)

### Acesse o IP criado pelo loadbalancer do fidelizamaisvoce-deployment-service.

![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/64f6305b-fc3b-4aad-ab87-a77c8abdb935)

### Ao acessar o navegado você acessara a pagina abaixo atraves da url http://20.232.217.215.
![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/d2b1c4dc-9c58-417d-933f-3a959d702d0e)

### Em caso qualquer falha/exclusão em um dos pods o nosso deployment junto ao replica set se encarregara de criar um novo pod da nossa aplicação python

![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/759601a0-4749-4169-9018-03c57a0116f6)

![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/13080c21-5cac-4876-86f9-cfb5cf5deb7b)

![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/a793f6ab-e5f9-4993-bff8-e58ec6f23351)

![image](https://github.com/victorf16/KubernetesFlaskApp/assets/102988977/fef7b438-2ff7-44ea-bdd3-bbc64ebd0260)



