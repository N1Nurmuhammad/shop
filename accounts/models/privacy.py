from django.db import modelsfrom uuid import uuid4def upload_location(instance, filename):    ext = filename.split('.')[-1]    if ext.lower() in ['doc', 'png', 'pdf', 'xml', 'jpeg', 'mp4', 'jpg', 'mov', 'm4v']:        file_path = 'privacy/{title}'.format(title='{}.{}'.format(uuid4().hex, ext))        return file_path    else:        raise Exception("unsupport format")class PrivacyModel(models.Model):    text = models.FileField(upload_to=upload_location, )