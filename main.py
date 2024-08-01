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

    words = extract_words_counts(comments)[:10]
    return {"words": [word[0] for word in words]}


@app.get("/endpoint3")
async def endpoint3():
    top_10_stories = HackerNewsAPI.get_top_stories()[:10]

    comments = []
    for story_id in top_10_stories:
        story_comments = HackerNewsAPI.get_comments(story_id)
        comments.extend(story_comments)
        comments.extend(get_kids(story_comments))

    words = extract_words_counts(comments)[:10]
    return {"words": [word[0] for word in words]}


def extract_words_counts(comments):
    words = {}

    for comment_id in comments:
        comment_txt = HackerNewsAPI.get_comment_text(comment_id)
        comment_txt = strip_tags(comment_txt)
        for word in comment_txt.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    return words

def get_kids(comments):
    ret_val = []
    for comment_id in comments:
        kids = HackerNewsAPI.get_comments(comment_id)
        if kids:
            ret_val.extend(kids)
            ret_val.extend(get_kids(kids))
    return ret_val
