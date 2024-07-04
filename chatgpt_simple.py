import openai
import time

openai.api_key = "my api key"

try:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "write an essay on python programming language"
            }
        ]
    )
    print(completion['choices'][0]['message']['content'])

except openai.error.RateLimitError as e:
    print(f"Rate limit exceeded. Waiting for reset...")
    # Retry after waiting for some time (e.g., 1 hour)--
    time.sleep(3600)  # Wait for 1 hour
    # Retry the API call
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "write an essay on python programming language"
            }
        ]
    )
    print(completion['choices'][0]['message']['content'])

except Exception as e:
    print(f"An error occurred: {str(e)}")
