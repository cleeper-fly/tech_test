## Requirements

 - Docker (tested on v24.0.5)
 - docker-compose (tested on v1.29.2)
 - All ports mentioned in docker-compose.yaml are open and not occupied. If some ports are unavailable, 
   please change them in docker-compose.yaml and .env files accordingly 

## Installation

 1) Clone this repository:\
    ```git clone https://github.com/cleeper-fly/tech_test``` 
 2) Navigate to the project directory:\
    ```cd tech_test``` 
 3) Add .app.env and .db.env files in the project directory. 
    Examples of variables are provided in .example files. 
    You can create .env from .example:\
    ```cat .app.env.example > .app.env``` \
    ```cat .db.env.example > .db.env``` 
 4) Start app:\
    ```docker compose up``` 
 5) Example of the required endpoint call:\
    ```curl --location 'http://localhost:8000/api/v1/genes?gene_symbol=JAG1'``` \
    Or you can use the automatic API docs:\
    ```http://localhost:8000/docs#/genes/get_genes_api_v1_genes_get```