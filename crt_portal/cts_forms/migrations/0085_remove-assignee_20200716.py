# Generated by Django 2.2.13 on 2020-07-16 15:26

from django.db import migrations
from datetime import datetime
import pytz
from actstream import action
from django.contrib.auth import get_user_model
from actstream import registry


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0084_form_template_standardization'),
    ]

    def unremove_assignee(apps, schema_editor):
        pass

    def remove_assignee(apps, schema_editor):
        User = get_user_model()
        userlist = User.objects.all().order_by('id')
        # // Assuming that first user is the root user or superuser. If there are no users, skip assignee removal
        if len(userlist) > 0:
            superuser = userlist[0]
            # get all reports
            reports = apps.get_model('cts_forms', 'Report')
            # Register Report to be streamed
            registry.register(reports)
            timezone = pytz.timezone("UTC")
            july1 = timezone.localize(datetime(2020, 7, 1))
            for report in reports.objects.all():
                # remove assignee for report closed date is before june 30 2020,
                if report.closed_date is not None:
                    if report.closed_date < july1:
                        report.assigned_to = None
                        report.save()
                        # Add the closed activity to activity stream
                        action.send(superuser, verb='Assignee Removed: ',
                                    description='Removed assignee for closed record before July 1, 2020',
                                    target=report)
    operations = [
        migrations.RunPython(remove_assignee, unremove_assignee),
    ]
