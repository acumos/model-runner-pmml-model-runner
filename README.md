ACUMOS
================================================================================
Copyright @ 2018 AT&T Intellectual Property. All rights reserved.
================================================================================
This Acumos software file is distributed by AT&T under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

This file is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

    
## Overview

This DataPipeline Service , manages a data flow on a set of services which  deliver streaming and batch data to  pluggable microservices 
which can be predictors, model builders, data transformers or any other kind which can take data from the pipeline, process it 
and put it back on the pipeline.

Pipelines are managed in "pools" , which is a organising structure to allow many pipelines to share the 
same datasource and other objects for projects/initiatives which tend to reuse the same datasources and other transformations

