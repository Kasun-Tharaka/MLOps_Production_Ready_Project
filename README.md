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

- if data drift is detected, fix it manually and update the database.(do resampling, if it not working try to increase the number of data)

-start the data transformation(implement feature engineering which done in notebook)
- output of data validation willa be the input for the data transformation.
- first update the constants for data transformation, then update the entity(config entity - proper paths foe my constants), then update the components
- inside etity, new file created as estimator(a class for target column encoding)
- update the pipeline for data transformation

- jump into the model training
- in notebook, we trained multiple models and done hyperparameter tuning manually. we need convert into modular coding. that manual task will automated by some pakage call neuro_mf. so we are ging to use it here.
- to use neuro_mf, have to write a yamal inside config files which we gonna use model & parameters.
- in the seperate folder called estimator, create a class for do predictions with the test data avoiding writing in the trainig pipeline
- first update the constants, and entities(config and artifacts), and components, and pipeline

- first model evaluation, model pusher to production (amazon S3), prediction pipeline
- for model evaluation, it requires model.pkl (in artifacts/trainer) and test.csv (from data ingersion) and difine a threshold for model accuracy.
- after evaluation, if the model accuracy is higher than the threshold value it returns True. this return value based for start next stage call model pusher.
- in first time going to run pipeline, in S3 there is no any model. so our first model should push through the model pusher, whatever accuracy is.
- when run pipeline again, there is a model in S3. at this point inside evaluation using test data evaluate both model and check whether what model perform better. If new train model's accuracy is higher then run model pusher. otherwise model pusher wont execute.
- starting evaluation updating constants and add AWS credentials into constants,
export credentials in cmd

export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

after create system environment variables for above credentials.
- create a file in configuration to make aws connection.(same as for mongodb)

- create another folder inside visa approval call cloud storage(with constructor file). inside this file contains all the operations happens on cloud, which are how to push model, get current model(file contains all of the operations about on AWS, but now we dont need to use all of those operations)

- cteate estimator file inside entity for estimate S3 producttion(uploaded) model, loading and making predictions to whether it is fine or not

- update entities(config & artifacts), and components, then trainig pipeline.

- model pusher do not need any constant, then go for update entities and update components then go for training pipeline.

- for model_prediction, first update constants and entities