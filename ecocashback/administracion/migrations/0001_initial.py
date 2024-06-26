# Generated by Django 5.0.6 on 2024-06-28 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('comuna_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('contenedor_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_contenedor', models.CharField(max_length=50)),
                ('capacidad', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('empresa_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recompensa',
            fields=[
                ('recompensa_id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('puntos_necesarios', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('rol_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.CharField(max_length=100)),
                ('cantidad_disponible', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TotalCantidadResiduos',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_residuo', models.CharField(max_length=50)),
                ('cantidad_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('evento_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('ubicacion', models.CharField(max_length=255)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('actividad_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.evento')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.region'),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('empleado_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.empresa')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('transaccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('puntos_usados', models.IntegerField()),
                ('recompensa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.recompensa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('suscripcion_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_suscripcion', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Residuo',
            fields=[
                ('residuo_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_residuo', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('fecha_recoleccion', models.DateTimeField()),
                ('puntos_calculados', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('puntos_id', models.AutoField(primary_key=True, serialize=False)),
                ('puntos', models.IntegerField(default=0)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='NotificacionLanzamiento',
            fields=[
                ('notificacion_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('newsletter_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('tipo_suscripcion', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='LogActividad',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('actividad', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Facturacion',
            fields=[
                ('factura_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_emision', models.DateTimeField()),
                ('monto_total', models.IntegerField()),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.empresa')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccion_id', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.comuna')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='CalculoCO2',
            fields=[
                ('co2_id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_co2', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administracion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('auditoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('accion', models.CharField(max_length=255)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.usuario')),
            ],
        ),
    ]
