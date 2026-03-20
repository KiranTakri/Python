import gzip
# with gzip.open("Datafile.txt.gzip","wt") as f:
#     f.write("Hello Stident\n")
#     f.write("Good Morning")
with gzip.open("Datafile.txt.gzip","rt") as f:
    print(f.read())