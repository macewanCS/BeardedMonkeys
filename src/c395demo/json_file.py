#!/usr/bin/env python
import csv
import re

def clean(string):
    st = ""
    acceptable = "<>/,.?;:'][{} -_)(*&^%$#@!\"+"
    for s in string:
        if ( not(re.match("^[A-Za-z0-9_-]*$", s)) ):
            if (s in acceptable):
                st += s
            continue
        st += s
    st = st.rstrip('\t\r\n')
    return st

def main():
    file_name = raw_input("Enter the filename: ")
        
    try:
        with open(file_name) as csvfile:
            file_in = csv.reader(csvfile, delimiter=',', quotechar='"')
            try:
                file_name = file_name[:-4]
                file_name += ".json"
                out = open(file_name, 'w')
            except:
                print("Can't write on the file")
                exit()
            app = raw_input("Enter the app name: ")
            cl = raw_input("Enter the model name: ")
            model = app
            model += "."
            model += cl

            out.write('[\n')

            pk = 0
            for line in file_in:
                if (line[:-1] == '\n'):
                    line = line.replace('\n','')
                    
                if( pk == 0 ):
                    col = line
                    pk += 1
                    continue
                out.write('\t{\n')
                out.write('\t\t"model": "' + model + '",\n')
                out.write('\t\t"pk": ' + str(pk) + ',\n')
                out.write('\t\t"fields": {\n')
                
                temp = line
                i = 0
                length = len(col) - 1
                for c in col:
                    c = clean(c)
                    temp[i] = clean(temp[i])
                        
                    out.write('\t\t\t"' + c + '": "' + temp[i] + '"')
                    if (i == length):
                        out.write('\n')
                    else:
                        out.write(',\n')
                    i += 1
                
                out.write('\t\t}\n')
                out.write('\t},\n')
                pk += 1
                
            out.write(']')

    except:
        print("Can't find the file")
        exit()

if __name__ == "__main__":
    main()
    
