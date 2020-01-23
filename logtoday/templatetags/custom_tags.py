import os
from datetime import datetime
from collections import OrderedDict
from django import template
from django.utils import timezone

from logtoday.models import DailyActivity

register = template.Library()


@register.inclusion_tag(
    os.path.join("dashboard", "_monthly_report.html")
)
def monthly_activities(month_year):
    m_activities = OrderedDict()
    month = datetime.strptime(month_year, "%m-%Y").date().month if month_year else timezone.now().month
    year = datetime.strptime(month_year, "%m-%Y").date().year if month_year else timezone.now().year
    try:
        activities = DailyActivity.objects.filter(activity_created__month=month, activity_created__year=year)
    except Exception:
        # log event, passing for now
        pass
    else:
        for activity in activities or []:
            if activity.activity_goal_map not in m_activities:
                m_activities[activity.activity_goal_map] = [activity]
            else:
                m_activities[activity.activity_goal_map].append(activity)
    return {
        'month': datetime.strptime(month_year, "%m-%Y") if month_year else timezone.now(),
        'goal_activities': m_activities
    }


@register.filter
def multiply(value, arg):
    return value * arg
