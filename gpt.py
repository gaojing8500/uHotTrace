import json
import openai

from prompt import web_analysise

API_KEY = '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'
openai.api_key = API_KEY

system_prompt = [{"role": "system", "content": web_analysise['system']}]
def generate_chunk_code_chat(messages,stream=False,model='gpt-3.5-turbo-16k'):
    predictions = openai.ChatCompletion.create(
                model=model,
                stream=stream,
                messages=messages,
                max_tokens=8096,
                top_p=0.2,
                frequency_penalty=1.3)
    return predictions
    # async for chunk in predictions:
    #     yield f"event: completion\ndata: {json.dumps(chunk)}\n\n"
    # yield "event: done\ndata: [DONE]\n\n"
def get_gpt_model_predict(messages,stream=None,model=None):
    user_prompt = [{"role": "user", "content": messages}]
    messages = system_prompt + user_prompt
    if stream:
        response = generate_chunk_code_chat(messages)
    else:
        response =  generate_chunk_code_chat(messages)
        resp = response["choices"][0]['message']['content']
        return resp





