# Google Cloud Survey Flask Application
This repo hosts a Flask application that has been deployed with continuous integration and delivery. This allows the application to be updated whenever code is pushed to this repository. This survey app simply asks users their favorite color and records answers from users.
The app can currently be accessed at: https://project1helloml.uc.r.appspot.com/

## Instructions 

1. In order to run the application, first create a new project in Google Cloud and ensure you are working in said project. If you are not, run the following:

```
gcloud config set project $GOOGLE_CLOUD PROJECT
```

2. Now git clone the repo to your directory of choice. 

```
HTTPS: git clone https://github.com/Nathan2Warren/GCP_Flask_app.git
SSH: git clone git@github.com:Nathan2Warren/GCP_Flask_app.git
```

3. Create a virtual environment.
```
virtualenv ./venv
source ./venv/bin/activate
```

4. All the required packages (requirements.txt) can be installed by simply running:
```
make install 
```

5. Create the GCP App Engine and select any region
```
gcloud app create
```

6. You can run the application locally to make sure it is working
```
python main.py
```

7. Or you can deploy the application on the cloud
```
gcloud app deploy
```

## References
[Noah Gift's GCP and Flask Tutorials](https://github.com/noahgift/cloud-data-analysis-at-scale/blob/master/topics/paas-continuous-delivery.md)
[Code Maven Flask Poll Tutorial](https://github.com/noahgift/cloud-data-analysis-at-scale/blob/master/topics/paas-continuous-delivery.md)
