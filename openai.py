from openai import OpenAI

client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
YOUR CHAT DATA HERE
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named user who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like user"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)
