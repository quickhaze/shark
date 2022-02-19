#!/usr/bin/env bash
chown ubuntu:ubuntu /home/ubuntu/tutor/shark
python -m venv /home/ubuntu/tutor/env
chown ubuntu:ubuntu /home/ubuntu/tutor/env
chown ubuntu:ubuntu /home/ubuntu/tutor/env/*
source /home/ubuntu/tutor/env/bin/activate
pip install -r /home/ubuntu/tutor/shark/requirements.txt