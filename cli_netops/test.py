import openai

# Set your OpenAI API key
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Provide a prompt for the model to continue
prompt = "Once upon a time in a land far, far away"

# Generate a completion based on the prompt
response = openai.Completion.create(
    engine="text-davinci-003",  # Engine ID (choose based on your needs)
    prompt=prompt,
    max_tokens=50  # Maximum length of generated text
)

# Print the generated text
print(response.choices[0].text.strip())
