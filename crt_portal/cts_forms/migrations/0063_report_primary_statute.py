# Generated by Django 2.2.11 on 2020-03-25 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0062_add_district_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='primary_statute',
            field=models.CharField(blank=True, choices=[('144', '144'), ('145', '145'), ('166', '166'), ('167', '167'), ('168', '168'), ('169', '169'), ('170', '170'), ('170-USE', '170-USE'), ('171', '171'), ('175', '175'), ('187', '187'), ('188', '188'), ('197', '197'), ('198', '198'), ('202', '202'), ('204', '204'), ('205', '205'), ('206', '206'), ('207', '207'), ('208', '208'), ('210', '210'), ('216', '216'), ('217', '217'), ('218', '218'), ('219', '219'), ('220', '220'), ('230', '230'), ('259', '259'), ('300', '300'), ('39', '39'), ('50', '50'), ('502', '502'), ('504', '504'), ('508', '508'), ('595', '595')], max_length=7, null=True),
        ),
    ]
