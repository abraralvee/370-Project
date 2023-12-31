# Generated by Django 4.2.7 on 2023-12-01 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingItem',
            fields=[
                ('Serial_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=10)),
                ('Condition', models.CharField(max_length=10)),
                ('Size', models.IntegerField()),
                ('Category', models.CharField(max_length=10)),
                ('Rent_status', models.CharField(max_length=10)),
                ('Gender', models.CharField(max_length=10)),
                ('Image', models.CharField(max_length=50, null=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('Transaction_iD', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('Total_payment', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Visa_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Card_number', models.IntegerField()),
                ('Transaction_iD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cloth.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reviews', models.CharField(max_length=50)),
                ('Serial_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cloth.clothingitem')),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('Address', models.CharField(max_length=80)),
                ('Email', models.CharField(max_length=30)),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cloth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Rentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shipping_address', models.CharField(max_length=80)),
                ('Email', models.CharField(max_length=30)),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cloth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Nagad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_no', models.CharField(max_length=15)),
                ('Transaction_iD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cloth.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cloth.user')),
            ],
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='Reviews',
            field=models.ManyToManyField(related_name='clothing_items', to='Cloth.review'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Voucher', models.CharField(max_length=10)),
                ('Total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Daily_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Delivery_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Duration', models.DurationField()),
                ('Cart_number', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cloth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bkash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_no', models.CharField(max_length=15)),
                ('Transaction_iD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cloth.transaction')),
            ],
        ),
    ]
