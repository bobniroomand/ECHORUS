import requests 


class HackerNewsAPI:
    TOP_STORIES_API = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    ITEM_API = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'

    def get_top_stories():
        response = requests.get(HackerNewsAPI.TOP_STORIES_API)
        top_stories = response.json()
        return top_stories
    
    def get_item(item_id):
        response = requests.get(HackerNewsAPI.ITEM_API.format(item_id))
        item = response.json()
        return item
    
    def get_comments(item_id):
        item = HackerNewsAPI.get_item(item_id)
        kids = item.get('kids', [])
        return kids

    def get_comment_text(comment_id):
        item = HackerNewsAPI.get_item(comment_id)
        text = item.get('text', '')
        return text
