import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/generate-story/", response_model=str)
async def generate_story(prompt: str):
    url = "https://api.openai.com/v1/engines/davinci/completions"
    headers = {
        "Authorization": f"Bearer YOUR_API_KEY_HERE"
    }
    json_data = {
        "prompt": prompt,
        "max_tokens": 150
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=json_data)
        if response.status_code == 200:
            return response.json()['choices'][0]['text']
        else:
            raise HTTPException(status_code=response.status_code, detail="Error from ChatGPT API")
