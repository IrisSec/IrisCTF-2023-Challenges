#!/bin/sh
python3 ./nginx.yaml.py
kubectl apply -f nginx.yaml
