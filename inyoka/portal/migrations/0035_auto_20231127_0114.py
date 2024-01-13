# Generated by Django 3.2.23 on 2023-11-27 01:14

from django.db import migrations


def remove_jabber_status(apps, schema_editor):
    User = apps.get_model("portal", "User")

    for u in User.objects.all():
        # remove `show_jabber` as it is not used for notifications anymore
        show_jabber = u.settings.pop('show_jabber', False)
        is_hidden = not show_jabber
        if is_hidden:
            # remove jabber-id, if it was private
            u.jabber = ''

        # no notifications possible via jabber anymore, so remove the setting
        if 'jabber' in u.settings.get('notify', []):
            u.settings['notify'].remove('jabber')

        u.save()


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0034_alter_user_jabber'),
    ]

    operations = [
        migrations.RunPython(remove_jabber_status),
    ]
