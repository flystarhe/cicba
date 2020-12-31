#!/bin/bash
set -e

TASK=${1:-dev}
if [ "${TASK}" != 'dev' ]
then
    nohup python "${TASK}/app_tornado.py" ${@:2} > "nohup.${TASK}" 2>&1
else
    jupyter notebook --ip='*' --port=9000 --notebook-dir='/workspace' --NotebookApp.token='hi' --no-browser --allow-root
fi
