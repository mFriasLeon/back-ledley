from django.db import migrations
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now


def create_superuser(apps, schema_editor):
    AuthUser = apps.get_model('auth', 'User')

    if not AuthUser.objects.filter(username='admin').exists():
        AuthUser.objects.create(
            username='admin',
            email='admin@example.com',
            is_staff=True,
            is_superuser=True,
            password=make_password('admin1234'),
        )


def delete_superuser(apps, schema_editor):
    AuthUser = apps.get_model('auth', 'User')
    AuthUser.objects.filter(username='admin').delete()


def create_test_users(apps, schema_editor):
    User = apps.get_model('user', 'User') 
    Patient = apps.get_model('user', 'Patient')
    Professional = apps.get_model('user', 'Professional')


    if not User.objects.filter(username='test_patient').exists():
        user_patient = User.objects.create(
            username='test_patient',
            email='patient@gmail.com',
            password=make_password('patient1234'),
            name = 'Test Patient',
            gender = "Male",
            birth_date = '1990-01-01',
            created_date = now(),
            active=True 

        )
        Patient.objects.create(user=user_patient)

    if not User.objects.filter(username='test_professional').exists():
        user_profesional = User.objects.create(
            username='test_professional',
            email='professional@example.com',
            password=make_password('professional1234'),
            name='Test Professional',
            gender = "female",
            birth_date = '1985-01-01',
            created_date = now(),
            active=True

        )
        Professional.objects.create(user=user_profesional,role='Physician')


def delete_test_users(apps, schema_editor):
    User = apps.get_model('user', 'User')
    Patient = apps.get_model('user', 'Patient')
    Professional = apps.get_model('user', 'Professional')

    Patient.objects.filter(user__username='test_paciente').delete()
    Professional.objects.filter(user__username='test_profesional').delete()

    User.objects.filter(username__in=['test_paciente', 'test_profesional']).delete()


class Migration(migrations.Migration):

    dependencies = [
          ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, delete_superuser),
        migrations.RunPython(create_test_users, delete_test_users),
    ]


