from fastapi import FastAPI

from hacker_news_api import HackerNewsAPI
from mlstriper import strip_tags

app = FastAPI()


@app.get("/endpoint1")
async def endpoint1():
    top_100_stories = HackerNewsAPI.get_top_stories()[:100]
    comments = []
    for story in top_100_stories:
        comments.extend(HackerNewsAPI.get_comments(story)[:50])
    return {"comments": comments}


@app.get("/endpoint2")
async def endpoint2():
    top_30_stories = HackerNewsAPI.get_top_stories()[:30]
    comments = []
    for story in top_30_stories:
        comments.extend(HackerNewsAPI.get_comments(story)[:100])
    
    words = {}

    for comment_id in comments:
        comment_txt = HackerNewsAPI.get_comment_text(comment_id)
        comment_txt = strip_tags(comment_txt)
        for word in comment_txt.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    words = sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]
    return {"words": [word[0] for word in words]}

