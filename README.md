# MLOps_Production_Ready_Project

## here we use:
- Anaconda
- VSCode
- Mongodb
- Github
- AWS
- Docker

### Create virtual environment with python 3.8

## Steps
- Create a virtual environment
- Create project template
- add requirements
- load dataset and setup DB connection(notebook)
- implement logging
- implement custom exception
- implement utils
- EDA(notebook)
- Feature Enineering(notebook)
- Model Training(notebook)
- Data Ingestion Component
    - set MONGODB_KEY as a system variable using export command on bash
- set the data ingestion component


1. constant
2. entity
3. cofiguration
4. component
5. pipeline






## spetial notes:
- Config_entity take the constat and give the proper path to the Data Ingestion Component. And data injection generates two outputs such as Train.csv and Test.csv and save them in the Artifacts folder.
- The output of the data injection component will be the input of the data validation component. there will be checks data in correct format and etc.
- Output of data validation component will send to the data transformation component.
- Output of data transformation component will send to the model trainer component.
- output of the model trainer component will send to the model evaluation component.
- Output of model evaluation component will send to the model pusher component.

- kept databse connection in a seperate file: when I need to make the connection, I just need to call the call name only. otherwise it will be messy writing code in same file.(OOP concept)

- then convert data into a data frame(inside seperate folder called data access) automated code, it can be used anywhere you want.

- data ingestion component is done.
- training pipeline is done.