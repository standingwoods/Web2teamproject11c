import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from django.contrib.auth.models import User
from tenrr.models import UserProfile, Post, Category, Like, Comment
from django.utils import timezone

def populate():
    # Create category
    graphic_design, _ = Category.objects.get_or_create(name='Graphic Design')
    digital_marketing, _ = Category.objects.get_or_create(name='Digital Marketing')
    writing_translation, _ = Category.objects.get_or_create(name='Writing & Translation')
    video_animation, _ = Category.objects.get_or_create(name='Video & Animation')
    audio_voiceovers, _ = Category.objects.get_or_create(name='Audio & Voiceovers')

    # Create users
    alice = User.objects.create_user('alice', 'alice@example.com', 'alicepassword')
    alice_profile = UserProfile.objects.create(user=alice, user_type='Seller')

    bob = User.objects.create_user('bob', 'bob@example.com', 'bobpassword')
    bob_profile = UserProfile.objects.create(user=bob, user_type='Seller')

    carol = User.objects.create_user('carol', 'carol@example.com', 'carolpassword')
    carol_profile = UserProfile.objects.create(user=carol, user_type='Buyer')

    dave = User.objects.create_user('dave', 'dave@example.com', 'davepassword')
    dave_profile = UserProfile.objects.create(user=dave, user_type='Buyer')

    Jack = User.objects.create_user('Jack', 'Jack@example.com', 'Jackpassword')
    Jack_profile = UserProfile.objects.create(user=Jack, user_type='Seller')

    Mary = User.objects.create_user('Mary', 'Mary@example.com', 'Marypassword')
    Mary_profile = UserProfile.objects.create(user=Mary, user_type='Buyer')

    Fish = User.objects.create_user('Fish', 'Fish@example.com', 'Fishpassword')
    Fish_profile = UserProfile.objects.create(user=Fish, user_type='Seller')

    Cow = User.objects.create_user('Cow', 'Cow@example.com', 'Cowpassword')
    Cow_profile = UserProfile.objects.create(user=Cow, user_type='Buyer')

    # Creat post
    post1 = Post.objects.create(
        title='Logo Design Tips',
        content='Some useful tips on creating a memorable logo',
        author=alice,
        category=graphic_design,
        created_date=timezone.now(),
        price=50.00
    )

    post2 = Post.objects.create(
        title='SEO Best Practices',
        content='Learn about the latest in SEO optimization',
        author=bob,
        category=digital_marketing,
        created_date=timezone.now(),
        price=75.00
    )

    post3 = Post.objects.create(
        title='Chinese translation',
        content='I can translate chinese to english',
        author=Jack,
        category=writing_translation,
        created_date=timezone.now(),
        price=66.00
    )

    post4 = Post.objects.create(
        title='Piano recording',
        content='I can play you an amazing piano recording。',
        author=Fish,
        category=audio_voiceovers,
        created_date=timezone.now(),
        price=999.00
    )

    # creat like and post
    like1 = Like.objects.create(post=post1, user=carol)
    comment1 = Comment.objects.create(post=post1, user=dave, text='Great tips! Thanks for sharing.')

    like2 = Like.objects.create(post=post2, user=dave)
    comment2 = Comment.objects.create(post=post2, user=carol, text='Really helpful article on SEO.')

    like3 = Like.objects.create(post=post3, user=Mary)
    comment3 = Comment.objects.create(post=post3, user=Mary, text='Good translation!')

    like4 = Like.objects.create(post=post4, user=Cow)
    comment4 = Comment.objects.create(post=post4, user=Cow, text='This guy is a terrible piano player！')

    print("Database has been added")

# Start execution here
if __name__ == '__main__':
    print("Starting population script...")
    populate()
