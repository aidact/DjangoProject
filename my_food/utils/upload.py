import os
import shutil


def document_path(instance, filename):
    user_id = instance.user_id
    return f'users/{user_id}/{filename}'


def user_delete_path(document):
    datetime_path = os.path.abspath(os.path.join(document.path, '..'))
    shutil.rmtree(datetime_path)