from shop.models import Category


def links(requests):
    c=Category.objects.all()
    return{'links':c}
