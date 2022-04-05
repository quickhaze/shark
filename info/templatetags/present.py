import datetime
from django import template

register = template.Library()

TODAY = datetime.date.today()


@register.simple_tag
def is_present(user):
    user_present = user.attendance.filter(
        created_at__year=TODAY.year,
        created_at__month=TODAY.month,
        created_at__day=TODAY.day,
    ).exists()
    if user_present:
        return "End Work"
    else:
        return "Start Work"


@register.simple_tag
def last_day_of_month(month=None):
    TODAY = datetime.date.today()
    if month:
        TODAY = TODAY.replace(month=month) 
    return (
        datetime.date(
            TODAY.year + (TODAY.month == 12),
            (TODAY.month + 1 if TODAY.month < 12 else 1),
            1,
        )
        - datetime.timedelta(1)
    ).day


@register.inclusion_tag("attendance.html")
def get_attendance(user, num):
    return {"object": user, "xl": user.look.attendance(num)}
