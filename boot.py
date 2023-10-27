import openai

open("run_0.py", "w").write(
    openai.ChatCompletion.create(
        api_key=open("key.txt").read(),
        model="gpt-3.5-turbo",
        temperature=0.001,
        messages=[
            {"role": "user", "content": open("prompt_0.txt").read()},
        ],
    )
    .choices[0]
    .message.content.replace("```", "#```")
)
