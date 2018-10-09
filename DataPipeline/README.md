#ACUMOS
#================================================================================
#Copyright @ 2018 AT&T Intellectual Property. All rights reserved.
#================================================================================
#This Acumos software file is distributed by AT&T under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#This file is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and 
#limitations under the License.
# DataPipeline Service

## Overview

This DataPipline Service , manages a data pipline delivering data to microservices plugged into the data pipeline.
The pipeline service will enable pipelines to be created via an api and manages the operation of a pipelie.
Pipelines are managed in "pools" , which is a organising structure to allow many pipelines to share the 
same datasource and other objects for projects/initiatives which tend to reuse the same datasources and other transformations

## Technical Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the DataPipline directory:

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```