from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField
from wtforms.validators import DataRequired


class UploadFileModel(FlaskForm):
    picture = FileField(
        "Загрузи свое фото, если не ссышься критики",
        validators=[FileAllowed(['jpg', 'png', 'webp', 'jpeg', 'JPG', 'PNG', 'JPEG']), DataRequired()]
    )

    submit = SubmitField("Заценить")
