prompt_library = [
"Explain Artificial Intelligence.",
"Explain Artificial Intelligence in simple language with examples.",
"Explain AI to first-year engineering students with "
"a definition, three real-world examples, and a conclusion."
]
# Human manually chooses the suitable prompt
selected_prompt = prompt_library[2]
task = "Prepare an introduction to Artificial Intelligence."
response = model.invoke(f"{selected_prompt}\nTask: {task}")
print(response.content)
