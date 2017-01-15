from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from webadmin.settings import LIST_PAGE_SIZE


def preparePage(request, dataList):
    page = 0
    if 'page' in request.GET:
        page = int(request.GET['page'])
    paginator = Paginator(dataList, LIST_PAGE_SIZE)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list
