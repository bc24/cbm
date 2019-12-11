import os

for filename in os.listdir(pfad_zum_ordner):
    os.remove(os.path.join(pfad_zum_ordner, filename))