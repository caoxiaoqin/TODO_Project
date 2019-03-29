from django.db import models


class TodoList(models.Model):
    thing = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    # user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    #
    # class Meta:
    #     managed = False
    #     db_table = 'tb_todo'

    def __str__(self):
        return self.thing
