from django.db import models
from django.conf import settings
from django.core.validators import EmailValidator, RegexValidator

from . import model_utils

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
        )
    email_confirmed = models.NullBooleanField(default=False)
    phone_number = models.CharField(max_length=16, null=True, blank=True, help_text="Please use the following format: <em>555-555-5555</em>")
    address1 = models.CharField(max_length=150, null=True, blank=True)
    address2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.PositiveIntegerField(null=True, blank=True)
    country = model_utils.CountryField(null=True, blank=True)
    enrollment_status = models.CharField(max_length=25, null=True, blank=True)
    payment_status = models.PositiveSmallIntegerField(null=True, blank=True)
    hours_purchased = models.PositiveSmallIntegerField(null=True, blank=True)
    hours_received = models.PositiveSmallIntegerField(null=True, blank=True)
    payrate = models.PositiveSmallIntegerField(null=True, blank=True)
    client_type = models.ForeignKey('ClientType', null=True, blank=True, on_delete=models.CASCADE)
    focus_area = models.CharField(max_length=50, null=True, blank=True)
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
    college_matriculated = models.CharField(max_length=150, null=True, blank=True)
    colleges_accepted = models.CharField(max_length=250, null=True, blank=True)
    scholarship_money = models.CharField(max_length=150, null=True, blank=True)
    law_school_matriculated = models.CharField(max_length=150, null=True, blank=True)
    law_schools_accepted = models.CharField(max_length=250, null=True, blank=True)
    class Meta:
        db_table = 'profiles'
    def __str__(self):
        return str(self.user)


class ClientType(models.Model):
    client_type = models.CharField(max_length=150, unique=True)
    class Meta:
        db_table = 'client_types'
    def __str__(self):
        return str(self.client_type)


class Test(models.Model):
    test_name = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'tests'
    def __str__(self):
        return str(self.test_name)


class Section(models.Model):
    section_name = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'sections'
    def __str__(self):
        return str(self.section_name)


class Subsection(models.Model):
    subsection_name = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'subsections'
    def __str__(self):
        return str(self.subsection_name)


class Subsubsection(models.Model):
    subsubsection_name = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'subsubsections'
    def __str__(self):
        return str(self.subsubsection_name)


class QuestionType(models.Model):
    type_code = models.CharField(max_length=10, unique=True)
    type_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'question_types'
    def __str__(self):
        return '(%s) %s' % (self.type_code, self.type_name)


class Question(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    subsection_id = models.ForeignKey(Subsection, on_delete=models.CASCADE)
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
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    student_answer = models.CharField(max_length=50)
    time_spent = models.PositiveSmallIntegerField(help_text="Mark down time spent in minutes. <em>Example: for 2 minutes 30 seconds mark down 2.5.</em>")
    guess = models.NullBooleanField()
    class Meta:
        db_table = 'results'
    def __str__(self):
        return '%s_%s_%s_%s' % (self.user_id, self.test_id, self.section_id, self.question_id)


class Observation(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    subsection_id = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    subsubsection_id = models.ForeignKey(Subsubsection, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    time_spent = models.PositiveSmallIntegerField(help_text="Mark down time spent in minutes. <em>Example: for 2 minutes 30 seconds mark down 2.5.</em>")
    notes = models.TextField(max_length=1000)
    class Meta:
        db_table = 'observations'
    def __str__(self):
        return '%s_%s_%s_%s_%s_%s' % (self.user_id, self.test_id, self.section_id, self.subsection_id, self.subsubsection_id, self.question_id)


class MathScoreConversion(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    num_correct = models.PositiveSmallIntegerField()
    score = models.PositiveSmallIntegerField()
    class Meta:
        db_table = 'math_score_conversions'
    def __str__(self):
        return '%s_%s_%s' % (self.test_id, self.num_correct, self.score)


class ReadingScoreConversion(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    num_correct = models.PositiveSmallIntegerField()
    score = models.PositiveSmallIntegerField()
    class Meta:
        db_table = 'reading_score_conversions'
    def __str__(self):
        return '%s_%s_%s' % (self.test_id, self.num_correct, self.score)


class WritingScoreConversion(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    num_correct = models.PositiveSmallIntegerField()
    score = models.PositiveSmallIntegerField()
    class Meta:
        db_table = 'writing_score_conversions'
    def __str__(self):
        return '%s_%s_%s' % (self.test_id, self.num_correct, self.score)
