from fastapi import FastAPI, HTTPException, status
from datetime import datetime
from santa import Santa
import aiofiles
from typing import List

app = FastAPI()


FILE = 'people.txt'


@app.post("/secret-santa")
async def secret(people: List[str], gift_date: datetime, should_save: bool = False):
    paired = Santa.pair_people(people)
    for sender, receiver in paired:
        await Santa.send_mail(sender, receiver, gift_date)

    if should_save:
        async with aiofiles.open(FILE, 'a') as file:
            await file.write("\n".join(people))

    return {"detail": "great success", "status": status.HTTP_200_OK}
