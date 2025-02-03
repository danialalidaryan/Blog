from Post.models import Post

def get_recent_posts(request):
    return {
        "recent_posts" : Post.objects.order_by("-Created")[:3]
    }