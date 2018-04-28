from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from tools.models import *
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)


class ClientTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ClientType, ClientTypeAdmin)


class TestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Test, TestAdmin)


class SectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Section, SectionAdmin)


class SubsectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subsection, SubsectionAdmin)


class SubsubsectionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subsubsection, SubsubsectionAdmin)


class QuestionTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(QuestionType, QuestionTypeAdmin)


class QuestionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Question, QuestionAdmin)


class ResultAdmin(admin.ModelAdmin):
    pass
admin.site.register(Result, ResultAdmin)


class ObservationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Observation, ObservationAdmin)


class MathScoreConversionAdmin(ImportExportModelAdmin):
    list_display = ('test_id', 'num_correct', 'score')
    list_filter = ('test_id',)
admin.site.register(MathScoreConversion, MathScoreConversionAdmin)


class ReadingScoreConversionAdmin(ImportExportModelAdmin):
    list_display = ('test_id', 'num_correct', 'score')
    list_filter = ['test_id']
admin.site.register(ReadingScoreConversion, ReadingScoreConversionAdmin)


class WritingScoreConversionAdmin(ImportExportModelAdmin):
    list_display = ('test_id', 'num_correct', 'score')
    list_filter = ['test_id']
admin.site.register(WritingScoreConversion, WritingScoreConversionAdmin)
