from django import template

register = template.Library()


@register.simple_tag
def sort_by_total_points(queryset):
    return sorted(
            queryset,
            key=lambda friend: friend.total_points,
            reverse=True)
