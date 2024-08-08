## installation 
Contains the tesr an 

## Requests
### 1. OpenAI compatible curl request
```
curl localhost:3000/v1/chat/completions \
    -X POST \
    -d '{
  "model": "tgi",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is deep learning?"
    }
  ],
  "stream": true,
  "max_tokens": 20
}' \
    -H 'Content-Type: application/json'
```

### 2. Streaming 
```
curl 172.17.0.1:9014/generate_stream \
    -X POST \
    -d '{
      "model": "CohereForAI/aya-101",
      "inputs":"What is Deep Learning in swahili?","parameters":{"max_new_tokens":20}}' \
    -H 'Content-Type: application/json'
```
 curl 172.17.0.1:9044/generate_stream \
    -X POST \
    -d '{"inputs":"What is Deep Learning in swahili?","parameters":{"max_new_tokens":20}}' \
    -H 'Content-Type: application/json'


curl 172.17.0.1:9014/v1/chat/completions \
    -X POST \
    -d '{
  "model": "tgi",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is deep learning?"
    }
  ],
  "stream": true,
  "max_tokens": 20
}' \
    -H 'Content-Type: application/json'