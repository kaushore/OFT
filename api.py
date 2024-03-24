import uvicorn
from typing import Union
from fastapi import FastAPI, Query
from openai import OpenAI



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello, World"}

@app.post("/gpt35/generate-code")
async def generateCodeForQuery(prompt: str):

    openAI_key = "sk-API_Key"

    client = OpenAI(
      api_key=openAI_key,  
    )   
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a programming assistant, skilled in generating code based on the description provided."},
        {"role": "user", "content": prompt}
      ]
    )
    code = completion.choices[0].message.content
    return code



@app.post("/gpt40/generate-code")
async def generateCodeForQuery(prompt: str):   

    openAI_key = "sk-API_Key"

    client = OpenAI(
      api_key=openAI_key,  
    )
    completion = client.chat.completions.create(
      model="gpt-4",
      messages=[
        {"role": "system", "content": "You are a programming assistant, skilled in generating code based on the description provided."},
        {"role": "user", "content": prompt}
      ]
    )
    code = completion.choices[0].message.content
    return code




if __name__ == "__main__":
  uvicorn.run(app, host = "localhost", port=9800)