from Post.models import Article

def get_recent_articles(request):
    return {
        "recent_articles" : Article.objects.order_by("-created")[:3]
    }