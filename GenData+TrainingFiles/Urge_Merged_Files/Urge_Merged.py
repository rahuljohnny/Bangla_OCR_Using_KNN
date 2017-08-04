filenames = ['CC1.txt', 'CC2.txt','SC1.txt', 'SC2.txt', 'SC3.txt', 'SC4.txt', 'cd.txt']
with open('classifications.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


filenames = ['CFI1.txt', 'CFI2.txt','SFI1.txt', 'SFI2.txt', 'SFI3.txt', 'SFI4.txt','fd.txt']
with open('flattened_images.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)


print "Merged!!"