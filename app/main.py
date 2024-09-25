from typing import Annotated

import uvicorn
from fastapi import FastAPI, Body, HTTPException, status

from completion_client import CompletionClient
from schemas import ResponseFormat

completion_client = CompletionClient()
app = FastAPI()


@app.post("/is_smart")
async def is_smart(task: Annotated[str, Body(embed=True)], goal: Annotated[str, Body(embed=True)]) -> ResponseFormat:
    result = await completion_client.is_smart(task, goal)
    if result:
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Не удалось получить ответ ожидаемой структуры от chatgpt.") from None


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8084)
