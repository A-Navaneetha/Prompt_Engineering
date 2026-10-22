from langchain.chat_models import init_chat_model
from pydantic import BaseModel
# Initialize the model
model = init_chat_model(
"llama-3.1-70b-versatile",
model_provider="groq",
api_key="YOUR_GROQ_API_KEY"
)
# Require a Boolean structured response
class PromptSelection(BaseModel):
selected: bool
selector = model.with_structured_output(PromptSelection)
# Prompt library
prompt_library = [
"You are a summarization expert. Summarize the given text clearly.",
"You are a translation expert. Translate the given text "
"into the requested language.",
"You are a question-answering expert. Answer the given "
"question accurately."
]
task_to_perform = "translation"
task = "Translate 'Good morning, how are you?' into Telugu."
# Automatically select a suitable prompt
for i in prompt_library:
selection_prompt = f"""
Task type: {task_to_perform}
User task: {task}
Candidate prompt: {i}
Is this candidate suitable for the task?
Return selected=True if suitable, otherwise False.
"""
result = selector.invoke(selection_prompt)
if result.selected:
final_prompt = f"{i}\nTask: {task}"
response = model.invoke(final_prompt)
print(response.content)
break
else:
print("Current prompt is not selected; continuing.")
