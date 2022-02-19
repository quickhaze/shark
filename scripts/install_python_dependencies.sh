#!/usr/bin/env bash
chown ubuntu:ubuntu /home/ubuntu/tt1/shark
python -m venv /home/ubuntu/tt1/env
chown ubuntu:ubuntu /home/ubuntu/tt1/env
chown ubuntu:ubuntu /home/ubuntu/tt1/env/*
source /home/ubuntu/tt1/env/bin/activate
pip install -r /home/ubuntu/tt1/shark/requirements.txt