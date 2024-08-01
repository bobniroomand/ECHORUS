from fastapi import FastAPI

from hacker_news_api import HackerNewsAPI

app = FastAPI()


@app.get("/endpoint1")
async def endpoint1():
    top_100_stories = HackerNewsAPI.get_top_stories()[:100]
    comments = []
    for story in top_100_stories:
        comments.extend(HackerNewsAPI.get_comments(story)[:50])
    return {"comments": comments}
