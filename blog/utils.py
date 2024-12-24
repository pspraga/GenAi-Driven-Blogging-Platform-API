# blog/utils.py

import openai

def generate_blog_content(prompt):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()
