from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.core.validators import EmailValidator, RegexValidator

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        primary_key=True
        )
    phone_number = models.CharField(max_length=16, help_text="Please use the following format: <em>555-555-5555</em>")
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.PositiveIntegerField(null=True, blank=True)
    enrollment_status = models.CharField(max_length=25)
    payment_status = models.PositiveSmallIntegerField(null=True, blank=True)
    hours_purchased = models.PositiveSmallIntegerField(default=0)
    hours_received = models.PositiveSmallIntegerField(default=0)
    payrate = models.PositiveSmallIntegerField(default=0)
    client_type = models.ForeignKey('ClientType', on_delete=CASCADE)
    focus_area = models.CharField(max_length=50)
    sat_diagnostic = models.PositiveIntegerField(null=True, blank=True)
    sat_diagnostic_reading_and_writing = models.PositiveIntegerField(null=True, blank=True)
    sat_diagnostic_math = models.PositiveIntegerField(null=True, blank=True)
    sat_best_practice = models.PositiveIntegerField(null=True, blank=True)
    sat_best_practice_reading_and_writing = models.PositiveIntegerField(null=True, blank=True)
    sat_best_practice_math = models.PositiveIntegerField(null=True, blank=True)
    sat_best_official = models.PositiveIntegerField(null=True, blank=True)
    sat_best_official_reading_and_writing = models.PositiveIntegerField(null=True, blank=True)
    sat_best_official_math = models.PositiveIntegerField(null=True, blank=True)
    sat_best_official_essay = models.PositiveIntegerField(null=True, blank=True)
    lsat_diagnostic = models.PositiveIntegerField(null=True, blank=True)
    lsat_best_practice = models.PositiveIntegerField(null=True, blank=True)
    lsat_best_official = models.PositiveIntegerField(null=True, blank=True)
    act_diagnostic = models.PositiveIntegerField(null=True, blank=True)
    act_best_practice = models.PositiveIntegerField(null=True, blank=True)
    act_best_official = models.PositiveIntegerField(null=True, blank=True)
    college_matriculated = models.CharField(max_length=150)
    colleges_accepted = models.CharField(max_length=250)
    scholarship_money = models.CharField(max_length=150)
    law_school_matriculated = models.CharField(max_length=150)
    law_schools_accepted = models.CharField(max_length=250)
    class Meta:
        db_table = 'profiles'
    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ClientType(models.Model):
    client_type = models.CharField(max_length=150)
    class Meta:
        db_table = 'client_types'
    def __str__(self):
        return self.client_type


class Test(models.Model):
    test_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'tests'
    def __str__(self):
        return self.test_name


class Section(models.Model):
    section_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'sections'
    def __str__(self):
        return self.section_name


class Subsection(models.Model):
    subsection_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'subsections'
    def __str__(self):
        return self.subsection_name


class QuestionType(models.Model):
    type_code = models.CharField(max_length=10)
    type_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'question_types'
    def __str__(self):
        return '(%s) %s' % (self.type_code, self.type_name)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subsection = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    question_number = models.PositiveIntegerField()
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=50)
    class Meta:
        db_table = 'questions'
    def __str__(self):
        return '%s_%s_%s_%s' % (self.test, self.section, self.subsection, self.question_number)


class Result(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    class Meta:
        db_table = 'results'
    def __str__(self):
