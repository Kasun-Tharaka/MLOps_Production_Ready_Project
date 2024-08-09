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
- to data validation, create the schema.yaml file based on the dataset.


1. constant
2. entity
3. component
4. pipeline
5. Main file/ End point





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
- training pipeline is done for data ingestion.
- data validation, is my ata correct format or not

- The Data Drift problem: after split the data into training and testing. The distribution of the training and testing data is not same.(very complex problem, accuracy would be very low)
- when it comes to computer vision, model trained with dog data, and when testing provide cat data. model not familiar with cat data.

- in validation, consider, whether the number of columns are same as the training data, is numerical columns are exist and categorical columns are exist. if all are true then go for data drift detection(if false raise exception).

-from data validation, it will give some outputs, need to next stage which is data transformation. 

- in validation, schema file -> based on the dataset and EDA you can create a schema
- update the constants, entities(config and artifacts), comonents, 

- data validation, if majority of columns are data drift, then return False. Otherwise majority of columns are not data drift, consider as not data drift, so return True.