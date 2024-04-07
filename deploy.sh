
model=defog/sqlcoder-7b-2
model=chatdb/natural-sql-7b
volume=$PWD/data
export token=Akatein2000@
docker run --gpus all \
    --shm-size 28g -p 8000:80 \
    -e HUGGING_FACE_HUB_TOKEN=$token \
    -v $volume:/data ghcr.io/huggingface/text-generation-inference:1.4 \
    --model-id $model --max-batch-prefill-tokens 1024



curl localhost:8888/v1/chat/completions \
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