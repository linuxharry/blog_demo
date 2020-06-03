# -*- coding: utf-8 -*-
from django import template
from ..models import Entry, Category, Tag

register = template.Library()


@register.simple_tag()
def get_recent_entries(num=5):
    return Entry.objects.all().order_by('-create_time')[:num]


@register.simple_tag()
def get_popular_entries(num=5):
    return Entry.objects.all().order_by('-visiting')[:num]


@register.simple_tag()
def get_categories(num=5):
    return Category.objects.all()


@register.simple_tag()
def get_entry_count_for_category(category_name):
    return Entry.objects.filter(category__name=category_name).count()


@register.simple_tag()
def archives():
    return Entry.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag()
def get_entry_count_of_date(year, month):
    return Entry.objects.filter(create_time__year=year, create_time__month=month).count()

@register.simple_tag()
def get_tags():
    return Tag.objects.all()
