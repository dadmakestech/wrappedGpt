import openai
import sys


# This is a wrapper for the OpenAI GPT-3 API. It takes a prompt as a command line argument and returns the response from the API.
def getGpt3Response(inputPrompt, max_tokens=1372, temp=.5, top_p=1, frequency_penalty=.6, presence_penalty=.5):
    
    openai.api_key = ""
    response = openai.Completion.create(model="text-davinci-003", prompt=inputPrompt, temperature=temp, max_tokens=1372, top_p=top_p, frequency_penalty=frequency_penalty, presence_penalty=presence_penalty)
    
    return response.choices[0].text

if len(sys.argv) < 2:
    print(-1)
    print("You must provide a prompt")
else:
    print(getGpt3Response(sys.argv[1]))
