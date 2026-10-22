prompts = {
"A": {"prompt": "Explain machine learning.",
"relevance": 6, "clarity": 7, "completeness": 3},
"B": {"prompt": "Explain machine learning simply with examples.",
"relevance": 8, "clarity": 9, "completeness": 7},
"C": {"prompt": "Explain ML to beginners with a definition, "
"three real-world examples, and applications.",
"relevance": 10, "clarity": 9, "completeness": 10}
}
for item in prompts.values():
item["score"] = (
item["relevance"] + item["clarity"] + item["completeness"]
)
best = max(prompts.values(), key=lambda item: item["score"])
selected_prompt = best["prompt"]
response = model.invoke(selected_prompt)
print(response.content)
