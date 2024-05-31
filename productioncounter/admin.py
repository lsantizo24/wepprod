from django.contrib import admin

from django.db import models
from .models import weeklyPlan

# ... (Your WeeklyPlan model definition)

admin.site.register(weeklyPlan)