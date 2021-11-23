from .models import Category


def menu_links(request):
	links = Category.objects.all()
	# print('links--', links)
	# print('dict--', dict(links=links))
	return dict(links=links)
