from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
model=init_chat_model(
model="llama3.1:latest",
model_provider="ollama",
api_key=apiKey
)
openEndedPromptTemplate=PromptTemplate(
    input_variables=["role","subject","topic","plagarism","grammar","audience"],
    template="act like a professional {role}. your goal is to write a long chapter on the topic {topic} from subject {subject} with plagarism level {plagarism}. Through out the chapter maintain grammar of level {grammar}. so that the audience of level {audience} in that subject can understand the concept easily."
)
final_prompt=openEndedPromptTemplate.format(role="university level professor",subject="Machine Learning",topic="Bias & Variance",plagarism="0%",grammar="beginner",audience="beginner")
response=model.invoke(final_prompt)
print(response.content)
