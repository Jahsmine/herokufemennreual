import os
import random
from flask import current_app
from PIL import Image
from nerual.gender import resolve


def make_gender_sentence(picture, picture_path_saved):
    save_picture(picture)
    picture_path = os.path.join(
        'static/profile_pics',
        picture_path_saved
    )
    out_sentence = resolve(picture_path)
    gender_quotes, flag, color = None, None, None
    if out_sentence:
        if out_sentence[0] == "male":
            gender_quotes = "male"
            flag = "danger"
            color = "none"
        if out_sentence[0] == "female":
            gender_quotes = "female"
            flag = "success"
            color = "none"
        if out_sentence[0] == "grablina":
            flag = "danger"
            color = "red"
            return "Добро пожаловать в суд доргой", flag, color
        if out_sentence[0] == "ivan":
            flag = "success"
            color = "none"
            return "Ты хоть и ссышь стоя но твои видео про курс рубля смотрю даже я", flag, color
    else:
        flag = "info"
        color = "none"
        return "Ха это куколд))", flag, color
    with open(gender_quotes, "r", encoding='utf-8') as f:
        lines = f.read().splitlines()
    gender_sentence = random.choice(lines)
    os.remove(picture_path)
    return gender_sentence, flag, color


def save_picture(file_picture):
    picture_period_path = os.path.join(
        current_app.root_path,
        'static/profile_pics',
        file_picture.filename
    )
    saved_image = Image.open(file_picture)
    saved_image.save(picture_period_path)
    return file_picture

