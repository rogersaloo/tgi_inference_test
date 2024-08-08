from openai import OpenAI

# init the client but point it to TGI
client = OpenAI(
    base_url="http://10.19.143.248:9064/v1",
    api_key="-"
)

chat_completion = client.chat.completions.create(
    model="dbrx",
    messages=[
        {"role": "system", "content": "You are a helpful assistant." },
        {"role": "user", "content": "Helloinswahili"}
    ],
    stream=True,
    max_tokens=1000,
)

# iterate and print stream
for message in chat_completion:
    print(message)

