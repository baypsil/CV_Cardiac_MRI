# CardioScan Backend Server

Code for launching fast-api server in python:
`uvicorn app:app --host 127.0.0.1 --port 8000`

Open in browser: `http://127.0.0.1:8000/docs`

Docker build image command:
`docker build -t gcr.io/cardio-scan/annotate-mri .`

Docker run container command:
`docker run -d --name cardioscan-server -p 8000:8000 gcr.io/cardio-scan/annotate-mri`

Configure GCloud SDK:
1. `gcloud auth login`
2. `gcloud auth configure-docker`

Push Docker Image to GCP Container Registry:
`docker push gcr.io/cardio-scan/annotate-mri`

Deploy container service in Cloud Run.
URL: https://cardio-scan-ajldnrgi7a-uc.a.run.app

Obtain ID Token from GCloud CLI:
1. `gcloud auth activate-service-account --key-file=.json`
2. `gcloud auth print-identity-token`

SightCom Server API Dashboard: 
https://console.cloud.google.com/home/dashboard?project=cardio-scan
