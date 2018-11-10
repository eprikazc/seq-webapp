import os
import tempfile

from django.core.files import File
from django.core.files.base import ContentFile

from char_analyzer.celery import app

from char_analyzer.pipeline_v0 import pipeline
from core.models import Job


@app.task
def calculate(job_id):
    job = Job.objects.get(pk=job_id)
    job.status = Job.CHOICE_PROGRESS
    job.save()
    try:
        df, heatmap_plot = pipeline(job.input_file.path)
        csv_file = ContentFile(df.to_csv())
        job.output_file.save('result.csv', csv_file)

        _, temp_file_name = tempfile.mkstemp(suffix='.png')
        try:
            fig = heatmap_plot.get_figure()
            fig.savefig(temp_file_name)
            django_file = File(open(temp_file_name, 'rb'))
            job.output_image.save('result.png', django_file)
        finally:
            os.remove(temp_file_name)

        job.status = Job.CHOICE_SUCCESS
        job.save()
    except Exception:
        job.status = Job.CHOICE_FAILED
        job.save()
        raise
