def reverse_file(filea, fileb):
    infile = open(filea, "r")
    outfile = open(fileb, "w")
    lines = infile.readlines()
    reverse = lines[::-1]
    outfile.writelines(reverse)