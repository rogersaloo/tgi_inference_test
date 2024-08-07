!#/bin/bash
model=microsoft/Phi-3-mini-4k-instruct
volume=$PWD/data # share a volume with the Docker container to avoid downloading weights every run

docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data \
    ghcr.io/huggingface/text-generation-inference:2.2.0 \
    --model-id $model