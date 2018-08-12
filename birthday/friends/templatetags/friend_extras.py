from django import template
from math import ceil, sqrt

register = template.Library()


@register.simple_tag
def sort_by_total_points(queryset):
    return sorted(
            queryset,
            key=lambda friend: friend.total_points,
            reverse=True)


@register.simple_tag
def sort_for_collage(queryset):
    sorted_by_points = sort_by_total_points(queryset)
    total_friends = len(sorted_by_points)
    size = ceil(sqrt(total_friends))

    count = 0
    collage_friends = []
    row_friends = []

    for friend in sorted_by_points:
        row_friends.append(friend)
        count += 1
        if count == size:
            count = 0
            collage_friends.append(row_friends)
            row_friends = []

    collage_friends.append(row_friends)

    return collage_friends
