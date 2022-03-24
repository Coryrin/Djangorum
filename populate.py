import os
import random
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangorum_site.settings')
django.setup()
from boards.models import Post, PostComment, ForumBoard

gen = Faker()

topics = ['Gaming', 'Auto', 'Anime/Manga', 'News', 'General', 'Technology']

def add_topic():
    t = ForumBoard.objects.get_or_create(title=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topic()

        # create data
        fake_title = gen.sentence()
        fake_slug = gen.sentence()
        fake_body = gen.text()

        Post.objects.get_or_create(post=top, title=fake_title, body=fake_body, slug=fake_slug)

def populateComments(N=5):
    for entry in range(N):
        posts = Post.objects.all()

        post = random.choice(posts)

        # create data
        postParent = post
        fake_body = gen.text()

        PostComment.objects.get_or_create(post=postParent, body=fake_body)

if __name__ == '__main__':
    populatePosts = int(input('How many posts do you need generated?: '))
    populateComm = int(input('How many comments do you need generated?: '))

    print('Populating database...')
    populate(populatePosts)
    populateComments(populateComm)
    print('Entries added.')
