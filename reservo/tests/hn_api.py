from hackernews import HackerNews
from .models import Story

hn = HackerNews()

for stories in hn.top_stories(limit=10):

    stories = hn.get_item(stories)
    print stories.title
    print stories.url
    print stories.score
    print stories.by
    print stories.submission_time
    print stories.item_id

    Story.objects.create(title=stories.title, url = stories.url, \
    score = stories.score, submitter = stories.by, \
    timestamp = stories.submission_time, hn_id = stories.item_id)
