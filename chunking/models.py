from django.db import models

# Create your models here.
class Sentence(models.Model):
    languages = ( ('ENG', 'ENGLISH'), ('HIN', 'Hindi') )
    sentence = models.CharField(max_length=200)
    language = models.CharField(max_length=3, choices=languages)

    def __str__(self):
        return self.sentence

class Chunk(models.Model):
    pos_options = ( ('NNP', 'NNP'), ('VB', 'VB') )
    chunk_options = ( ('B-NP', 'B-NP'), ('B-VP', 'B-VP') )
    sentence = models.ForeignKey('Sentence', on_delete=models.CASCADE)
    index = models.IntegerField()
    word = models.CharField(max_length=100)
    pos = models.CharField(max_length=10, choices=pos_options)
    chunk = models.CharField(max_length=10, choices=chunk_options)

    def __str__(self):
        return '[' + self.word + ' || ' + self.pos + ' | ' + self.chunk + ']'
    