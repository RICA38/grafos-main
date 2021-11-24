import csv



# import os 
# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))




from models import Tejido

fields = ["temperatura", "color", "inflammation"]

for row in csv.reader(open('db.csv')):
    Tejido.objects.create(**dict(zip(fields, row)))