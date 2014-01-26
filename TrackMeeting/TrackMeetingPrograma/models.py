from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45L, db_column='Nombre') # Field name made lowercase.
    descripcion = models.CharField(max_length=100L, db_column='Descripcion', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'cliente'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200L)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class Empleado(models.Model):
    idempleado = models.IntegerField(primary_key=True, db_column='idEmpleado') # Field name made lowercase.
    nombre = models.CharField(max_length=45L, db_column='Nombre', blank=True) # Field name made lowercase.
    empresa_idempresa = models.ForeignKey('Empresa', db_column='Empresa_idEmpresa') # Field name made lowercase.
    apellido = models.CharField(max_length=45L, db_column='Apellido') # Field name made lowercase.
    class Meta:
        db_table = 'empleado'

class Empresa(models.Model):
    idempresa = models.IntegerField(primary_key=True, db_column='idEmpresa') # Field name made lowercase.
    nombre = models.CharField(max_length=45L, db_column='Nombre', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'empresa'

class Reunion(models.Model):
    id_reunion = models.IntegerField(primary_key=True)
    hora = models.TextField(db_column='Hora', blank=True) # Field name made lowercase. This field type is a guess.
    duracion = models.IntegerField(null=True, db_column='Duracion', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='Fecha', blank=True) # Field name made lowercase.
    direccion = models.CharField(max_length=45L, db_column='Direccion', blank=True) # Field name made lowercase.
    descripcion = models.CharField(max_length=45L, db_column='Descripcion', blank=True) # Field name made lowercase.
    motivo = models.CharField(max_length=45L, db_column='Motivo', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=45L, db_column='Estado', blank=True) # Field name made lowercase.
    empleado_idempleado = models.ForeignKey(Empleado, null=True, db_column='Empleado_idEmpleado', blank=True) # Field name made lowercase.
    cliente_id_cliente = models.ForeignKey(Cliente, db_column='Cliente_id_cliente') # Field name made lowercase.
    class Meta:
        db_table = 'reunion'