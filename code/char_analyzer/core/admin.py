from django.contrib import admin
from django.utils.safestring import mark_safe

from core.models import Job
from core.tasks import calculate


def run_jobs(modeladmin, request, queryset):
    for job in queryset:
        calculate.delay(job.id)
    modeladmin.message_user(
        request, '%s calculation job(s) added' % queryset.count())


run_jobs.short_description = 'Calculate'


class JobAdmin(admin.ModelAdmin):

    fields = ['input_file', 'output_file', 'image_tag']
    list_display = ['created_at', 'status_name', 'input_file']
    ordering = ['-created_at']
    actions = [run_jobs]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['input_file', 'output_file', 'image_tag']
        else:
            return ['output_file', 'image_tag']

    def image_tag(self, obj):
        return mark_safe('<img src="%s" />' % obj.output_image.url)
    image_tag.short_description = 'Image'

    def status_name(self, obj):
        return obj.get_status_display()
    status_name.short_description = 'Status'


admin.site.register(Job, JobAdmin)
