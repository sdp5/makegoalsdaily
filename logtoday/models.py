from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

TABLE_PREFIX = 'lt_'


class GoalsCategory(models.Model):
    """
    Goal Categories Model
    """

    category_id = models.AutoField(primary_key=True)
    category_value = models.CharField(max_length=200, unique=True, verbose_name="Goal Category (Slug Form)")
    category_name = models.CharField(max_length=500, verbose_name="Goal Category Name")

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('goal-category')

    class Meta:
        db_table = TABLE_PREFIX + 'categories'
        verbose_name_plural = "Goal Categories"


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
    goal_weight = models.IntegerField(
        verbose_name="Hours per day", default=2,
        validators=[MaxValueValidator(3), MinValueValidator(1)], null=True, blank=True
    )

    @property
    def days_remaining(self):
        return (self.goal_target - timezone.now()).days

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
    activity_created = models.DateTimeField(verbose_name="Activity Created On", default=timezone.now())
    activity_detail = models.CharField(max_length=1000, verbose_name="Describe Activity")
    activity_star = models.BooleanField(verbose_name="Mark this as milestone.")
    activity_goal_map = models.CharField(max_length=500, verbose_name="Map with Goal")
    activity_user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_weightage = models.IntegerField(
        verbose_name="Weights (4 Hours is 1 Weight)", default=1,
        validators=[MaxValueValidator(3), MinValueValidator(1)], null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse('activities-list')

    def __str__(self):
        return self.activity_detail

    class Meta:
        db_table = TABLE_PREFIX + 'activities'
        verbose_name_plural = "Daily Activities"
        ordering = ['-activity_created']
