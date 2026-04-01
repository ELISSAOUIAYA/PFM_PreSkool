
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_auth', '0005_alter_passwordresetrequest_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',

            field=models.CharField(default='VGI8FOD6zmzIzWxOVNdQSYUIL5Ap66St', editable=False, max_length=32, unique=True),

            field=models.CharField(default='3RbWG4yuBdbEOlSto43Ku73ExXIYf7Zg', editable=False, max_length=32, unique=True),

        ),
    ]
