from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
