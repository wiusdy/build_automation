#!/bin/bash

ACTION=$1
IMAGE=$2

if [ "$ACTION" = "push" ]; then
    echo "[MOCK] Pretending to push image: $IMAGE to ECR"
    echo "{ 'image': '$IMAGE', 'status': 'mock-pushed' }"
else
    echo "[MOCK] Unsupported action"
fi
