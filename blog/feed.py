# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
# from django.urls import reverse
from .models import Entry


class LatestEntriesFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "我的博客网站"
    # 通过聚合阅读器跳转到网站的地址
    link = "/siteblogs/"
    # 显示在聚合阅读器上的描述信息
    description = "最新更新的博客文章！"

    # 需要显示的内容条目
    def items(self):
        return Entry.objects.order_by('-create_time')[:5]

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return item.title

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.abstract

    # item_link is only needed if entries has no get_absolute_url method.
    # def item_link(self, item):
    #     return reversed('new-item', args=[item.pk])
