import os

def integratetxt(files_path = r'D:/dirname', file_prefix='filenameprefix', file_suffix='-extract.txt'):
    number_of_txt_files = 0
    for i in os.listdir(files_path):
        if os.path.splitext(i)[-1] != '.txt':
            continue
        number_of_txt_files += 1

    outputfile = os.path.join(files_path, file_prefix + 'whole.txt')
    with open(outputfile, 'a', encoding='utf-8') as f:
        for i in range(number_of_txt_files):
            
            filename = file_prefix + str(i) + file_suffix
            filepath = os.path.join(files_path, filename)
            print('Merging ' + filepath + ' into ' + outputfile)
            with open(filepath, 'r', encoding='utf-8') as ftemp:
                f.write(ftemp.read())
    
integratetxt()
