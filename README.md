## Client Service
This repository, _Client Service_, represents a part of a bigger project of a food ordering simulation,
performed as laboratory work during the _Network Programming_ course. Other components of
this project are: 
[_Dinning Hall_](https://github.com/MrCrowley21/Dinning_Hall.git),
[_Kitchen_](https://github.com/MrCrowley21/Kitchen.git), and
[_Food Ordering Service_](https://github.com/MrCrowley21/Food_Ordering_System.git) .\
!**Note** the fact that this version of README file is not final and will be modified  further.\
First, to run the project into a docker container, perform the following commands:
```` 
$ docker build -t client_service_image .  
$ docker run --net restaurant_network -p 5003:5003 --name client_service_container client_service_image
````
The first line will create an image of our project, while the next one - run project inside 
the created container. \
**NOTE** that the correct order of running the elements into the Docker container is the following: run the
command to create network, run the _Food Ordering Service_, run the _Kitchen_ component, run the _Dinning Hall_
component, and, in the end, run the Docker for _Client Service_ project.

For this moment, for more explanation regarding the code itself, please take a look at the comments 
that appears there.