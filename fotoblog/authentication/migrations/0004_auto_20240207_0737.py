# Generated by Django 5.0.1 on 2024-02-07 07:37

from django.db import migrations

def assign_blog_permissions(apps, schema_migration):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    add_blog = Permission.objects.get(codename='add_blog')
    change_blog = Permission.objects.get(codename='change_blog')
    delete_blog = Permission.objects.get(codename='delete_blog')
    view_blog = Permission.objects.get(codename='view_blog')

    creators = Group.objects.get(name='creators')
    creators.permissions.add(add_blog)
    creators.permissions.add(change_blog)
    creators.permissions.add(delete_blog)
    creators.permissions.add(view_blog)

    subscribers = Group.objects.get(name='subscribers')
    subscribers.permissions.add(view_blog)

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20240130_1449'),
    ]

    operations = [
        migrations.RunPython(assign_blog_permissions)
    ]