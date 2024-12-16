from multiprocessing import context
from django.shortcuts import render
from .my_post import post


def post_details(request, post_id):
    post_list = None
    for all_post in post:
        if all_post['id'] == post_id:
            post_list = all_post

    context = {
        'post': post_list
    }


    return render(request, 'blog/post_details.html', context=context)