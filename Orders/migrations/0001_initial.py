# Generated by Django 4.0 on 2022-04-06 11:47

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('country_code', models.CharField(blank=True, max_length=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total_paid', models.DecimalField(decimal_places=2, max_digits=5)),
                ('id_trasaction', models.CharField(max_length=200, verbose_name='ID transaction')),
                ('billing_status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='PayementMethode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ORANGE MONEY (OM)', 'ORANGE MONEY'), ('MOBILE MONEY (MM)', 'MOBILE MONEY'), ('USDT (TETHER)', 'USDT (TETHER)'), ('BITCOIN (BTC)', 'BITCOIN (BTC)'), ('Tron (TRC20)', 'Tron (TRC20)')], max_length=150, unique=True)),
                ('name_of_the_beneficiary', models.CharField(max_length=250, null=True)),
                ('number_id', models.CharField(max_length=150, null=True, unique=True)),
                ('image', pyuploadcare.dj.models.ImageField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='Stores.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment_option',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, related_name='payment_option', to='Orders.payementmethode'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to='Accounts.account'),
        ),
    ]
