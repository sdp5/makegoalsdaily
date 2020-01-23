from datetime import datetime

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
    goal_slug = models.SlugField(max_length=500, unique=True, verbose_name="Goal Name (Slug Form)")
    goal_desc = models.CharField(max_length=2000, verbose_name="Short Description", null=True, blank=True)
    goal_status = models.BooleanField(verbose_name="Goal Achieved?", default=False)
    goal_updated = models.DateTimeField(null=True, blank=True, verbose_name="Last Updated On")
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

    def save(self, *args, **kwargs):
        self.goal_updated = timezone.make_aware(
            datetime.now(), timezone.get_default_timezone()
        )
        return super(ShortTermGoals, self).save(*args, **kwargs)

    class Meta:
        db_table = TABLE_PREFIX + 'goals'
        verbose_name = "Short Term Goal"


class DailyActivity(models.Model):
    """
    Daily Activity Modal
    """

    activity_id = models.AutoField(primary_key=True)
    activity_created = models.DateTimeField(verbose_name="Activity Created On")
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

    def save(self, *args, **kwargs):
        if not self.activity_id:
            self.activity_created = timezone.make_aware(
                datetime.now(), timezone.get_default_timezone()
            )
        return super(DailyActivity, self).save(*args, **kwargs)

    class Meta:
        db_table = TABLE_PREFIX + 'activities'
        verbose_name_plural = "Daily Activities"
        ordering = ['-activity_created']


class GoalTasks(models.Model):
    """
    Goal Tasks Model
    """

    task_id = models.AutoField(primary_key=True)
    task_subject = models.CharField(max_length=400, verbose_name="Task Subject")
    task_details = models.CharField(max_length=1000, verbose_name="Task Details")
    task_created_on = models.DateTimeField(verbose_name="Activity Created On")
    task_target_date = models.DateTimeField(verbose_name="Task Target Date")
    task_completion_date = models.DateTimeField(verbose_name="Task Completion Date", null=True, blank=True)
    task_goal_map = models.CharField(max_length=500, verbose_name="Map with Goal")
    task_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_subject

    def save(self, *args, **kwargs):
        if not self.task_id:
            self.task_created_on = timezone.make_aware(
                datetime.now(), timezone.get_default_timezone()
            )
        return super(GoalTasks, self).save(*args, **kwargs)

    class Meta:
        db_table = TABLE_PREFIX + 'tasks'
        verbose_name_plural = "Goal Tasks"
        ordering = ['task_target_date']
