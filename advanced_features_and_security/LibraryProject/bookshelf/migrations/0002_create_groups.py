from django.db import migrations

def create_group(apps , schema_editor):
    Group = apps.get_model('auth','Group')
    Group.objects.get_or_create(name = 'Editors')
    Group.objects.get_or_create(name = 'Viewers')
    Group.object.get_or_create(name = 'Admins')

    class Migration(migrations.Migration):
        dependancies = [('bookshelf','0001_initial'),
                        ]
        operations = [
            migrations.RunPython(create_group)
        ]