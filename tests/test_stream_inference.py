from openai import OpenAI

# init the client but point it to TGI
client = OpenAI(
    base_url="http://172.28.0.1:9064/v1",
    api_key="-"
)

chat_completion = client.chat.completions.create(
    model="tgi",
    messages=[
        {"role": "system", "content": "You are a helpful assistant." },
        {"role": "user", "content": "Write 500 word essay about Nairobi"}
    ],
    stream=False,
    seed=42,
    max_tokens=1000,
)

# iterate and print stream
for message in chat_completion:
    print(message)