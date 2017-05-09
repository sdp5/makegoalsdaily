from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

TABLE_PREFIX = 'lt_'


class ShortTermGoals(models.Model):
    """
    Short term Goals Model
    """

    goal_id = models.AutoField(primary_key=True)
    goal_slug = models.CharField(max_length=500, unique=True, verbose_name="Goal Name (Slug Form)")
    goal_desc = models.CharField(max_length=2000, verbose_name="Short Description", null=True, blank=True)
    goal_status = models.BooleanField(verbose_name="Goal Achieved?", default=False)
    goal_updated = models.DateTimeField(null=True, blank=True, verbose_name="Last Updated On", default=timezone.now())
    goal_target = models.DateTimeField(null=True, blank=True, verbose_name="Expected Completion Date")
    goal_category = models.CharField(max_length=500, verbose_name="Goal Category")
    goal_notes = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Notes or Remarks")

    def __str__(self):
        return self.goal_slug

    def get_absolute_url(self):
        return reverse('goals-list')

    class Meta:
        db_table = TABLE_PREFIX + 'goals'
        verbose_name = "Short Term Goal"


class DailyActivity(models.Model):
    """
    Daily Activity Modal
    """

    activity_id = models.AutoField(primary_key=True)
    activity_created = models.DateTimeField(verbose_name="Activity Created On")
    activity_detail = models.CharField(max_length=1000, verbose_name="Activity")
    activity_star = models.BooleanField(verbose_name="Mark this as milestone.")
    activity_goal_map = models.CharField(max_length=500, verbose_name="Goal Nick Name")
    activity_user = models.CharField(max_length=500, verbose_name="Activity User")
    activity_weightage = models.IntegerField(verbose_name="Activity Weightage", null=True, blank=True)

    def __str__(self):
        return "{0} {1}".format(self.activity_id, self.activity_created)

    class Meta:
        db_table = TABLE_PREFIX + 'activities'
        verbose_name_plural = "Daily Activities"
