# IAyCienciaA#

[![DOI] DOI: 10.5281/zenodo.7709763

# Main
This Python script will read the .pdf files from the folder./open-access-articles and will Create some files on ./results. The input folder must contain papers in pdf
 format. The program will return three types of results. The first one will be keyword clouds created with the abstract of the file, the second type of result will 
 will show a bar chart showing the number of figures in each pdf, the last one is a histogram which will show the number of figures each file contains.
 

# Build and Run

## Requirements
It is necessary to have a Grobid server installed correctly and running on your machine, which by default will be running at the address http://localhost:8070.
This code has been developed and tested with Python 3.9.12 and pip 21.2.4.

## Docker

- Build the image
```
docker build -t <name_dockerFile> .
```
`name_dockerFile`  the name of the dockerFile 

- Run the container 
```
docker run --network=host -v </path/to/my_folder:/path/in/the/container> <name_dockerFile> <path_pdfs>
```
`--network` specify the network to be used by the container

`-v` mount a directory or file from the host machine into the container

`name_dockerFile`  the name of the dockerFile 

`path_pdfs` the path to the directory where the PDFs are located.

Examples: 

```
docker build -t dockerfile
docker  run --network=host -v C:/Users/ramon/IAOS:/app dockerfile /app/pdfs
```
# Environment
In case you are not using docker, you can create a conda environment to work with this script, open the terminal and follow the next instructions
- Install Conda: If you don't have Conda installed yet, install it from the official Anaconda website: https://www.anaconda.com/products/distribution
- Create a new environment: 
 ```
 conda create --n <name_enviroment>
 ```
 - Activate the environment: 
 ```
 conda activate <name_enviroment>
  ```
 - Install the following dependencies
   ```
   conda install grobid_client_python
   ```
   ```
   conda install wordcloud
   ```
   ```
   conda install matplotlib.pyplot
   ```
   ```
   conda install requests
   ```
   ```
   conda install re
   ```
   ```
   conda install os
   ```
 - Execute the program
   
   ```
   python IAOS.py <path_pdfs>
   ```

When you have finished working in the environment, you can deactivate it with the following command:
 ```
 conda deactivate 
 ```
 
 
 ## License and contact

Distributed under [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0). 

Main author and contact: Patricia Cifrián Pérez
