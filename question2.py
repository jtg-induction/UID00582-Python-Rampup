# Question: Write a program that returns the file type from a file name. 
# The type of the file is determined from the extension. Initially, a list of values of the form "extension,type"(e.g. xls,spreadsheet; png,image) will be input.
# The program takes input in the following form:
# Input extension and type values in the form of a string having the following format:
# "extension1,type1;extension2,type2;extension3,type3"
# E.g. If we needed to input xls → spreadsheet, xlsx → spreadsheet, jpg → image our string would be something like: "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
# Input a list of filename.extension. E.g. an input list could be something like ["abc.html", "xyz.xls", "text.csv", "123"]
# The program should return a dict of filename: type pairs 
# E.g.
# f("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg", "xyz.xls", "text.csv", "123"]) should return 
# {
#     "abc.jpg": "image",
#     "xyz.xls": "spreadsheet",
#     "Text.csv": "unknown",
#     "123": "unknown"}

# Function with required logic
def get_types(extension_types, files):
    ext_type_mapping = {}
    filename_extensions = {}

    try:
        ext_type_mapping = {key:value for key,value in (ext_types.split(',') for ext_types in extension_types.split(';'))}
    except:
        print("Pleaes provide the extensions and their types in proper format. Exiting...")
        return

    for file in files:
        extension = None
        try:
            extension = file.split('.', 1)[1]  # files with extension having double . like .aspx.cs will also be handled 
        except:
            extension = ""

        if(extension != ""):
            filename_extensions[file] = ext_type_mapping.get(extension, "unknown")
        else:
            filename_extensions[file] = "unknown"

    return filename_extensions


extension_types = input("Input extension,type; in provided format with no spaces: ")
files = input("Input space separated filename with extensions: ").split()
filename_type = get_types(extension_types, files)

if(filename_type):
    print("The filename and their types are as follows:\n", filename_type)
