#!/bin/bash
pip install virtualenv
virtualenv conversation-env
source conversation-env/bin/activate
conversation-env/bin/pip install -e library/grpc-google-cloud-conversation-v1alpha
conversation-env/bin/pip install -e library/gapic-google-cloud-conversation-v1alpha
pip uninstall -y certifi && pip install certifi==2015.04.28
pip install Flask
