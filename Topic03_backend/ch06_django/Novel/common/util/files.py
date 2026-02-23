import os


def handle_file(instance, file_field_name: str, *args, **kwargs):
    """rename the file to id when saving"""

    # check if the field exists, if not than return
    if not file_field_name:
        super(instance.__class__, instance).save(*args, **kwargs)
        return

    # get the file path from the database if exists
    old_instance = instance.__class__.objects.filter(id=instance.id).first()
    old_file_obj = None
    if old_instance:
        old_file_obj = getattr(old_instance, file_field_name)
    if old_file_obj:
        old_file_path = old_file_obj.path.replace("\\", "/")
    else:
        old_file_path = None

    # if user uploaded the file
    if getattr(instance, file_field_name):
        super(instance.__class__, instance).save(*args, **kwargs)
        file_obj = getattr(instance, file_field_name)

        pre_file_name = os.path.basename(file_obj.path.replace("\\", "/"))
        ext = os.path.splitext(pre_file_name)[-1]
        new_file_name = f"{instance.id}{ext}"

        pre_file_path = file_obj.path.replace("\\", "/")
        new_file_path = os.path.join(os.path.dirname(pre_file_path),
                                     new_file_name).replace("\\", "/")

        # if pre_file_path = new_file_path, means that file no changes
        # because the save function will rename the file if the filename exits
        if pre_file_path != new_file_path:
            if os.path.exists(new_file_path):
                os.remove(new_file_path)

            # if old file exists, removed it
            if (old_file_path and os.path.exists(old_file_path)):
                os.remove(old_file_path)

            # rename the prefile
            print(pre_file_path, new_file_path)
            os.rename(pre_file_path, new_file_path)
            file_obj.name = os.path.join(
                os.path.dirname(file_obj.name.replace("\\", "/")),
                new_file_name)
    elif instance.id:
        # check if the user saved the avatar before,
        # if yes, then delete it
        if old_file_path and os.path.exists(old_file_path):
            os.remove(old_file_path)

    super(instance.__class__, instance).save(*args, **kwargs)


def delete_file(fieldfile):
    """Check if the file exists, if yes, then delete it"""
    if fieldfile and os.path.isfile(fieldfile.path):
        os.remove(fieldfile.path)
