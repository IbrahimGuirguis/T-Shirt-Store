from django.db import models

class AboutUs(models.Model):
    about_intro_first_paragraph = models.TextField()
    about_intro_second_paragraph = models.TextField()
    about_image_left_text_head = models.TextField()
    about_image_left_text_paragraph = models.TextField()
    about_image_right_first_paragraph = models.TextField()
    about_image_right_second_paragraph = models.TextField()
    about_middle_head = models.TextField()
    about_middle_paragraph = models.TextField()
    about_last_section_head = models.TextField()
    about_last_section_first_paragraph = models.TextField()
    about_last_section_second_paragraph = models.TextField()