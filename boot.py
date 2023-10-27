import openai

exec(
    openai.ChatCompletion.create(
        api_key=open("key.txt").read(),
        model="gpt-3.5-turbo",
        temperature=0.001,
        messages=[
            {"role": "user", "content": open("boot.txt").read()},
        ],
    )
    .choices[0]
    .message.content.replace("```", "#```")
)
