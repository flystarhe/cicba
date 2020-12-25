#!/bin/bash
set -e

TASK=${1:-idcard}
nohup python "${TASK}/app_tornado.py" ${@:2} > "nohup.${TASK}" 2>&1
