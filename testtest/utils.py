import os
import csv
import sys
from some_project.settings import MEDIA_ROOT

def data_import(model, filename=None):
    name = filename if filename is not None else model.__name__
    path = os.path.join(MEDIA_ROOT, '%s.csv' % name)
    with open(path, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter="\t")
        try:
            bulk = [model(**i) for i in reader]
            model.objects.bulk_create(bulk)
            answer = True
        except Exception:
            answer = str(sys.exc_info())
        csvfile.close()
    return answer