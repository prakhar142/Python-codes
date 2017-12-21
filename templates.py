# os module is used to interact with operating system
import os

"""
/abc/ad/file.txt
\hi\this\ois\a\file.txt


open("hi\hi\this\ois\a\file.txt").read()

open("/abc/ad/file.txt").read()
"""
#os.path.join() -takes path whatever we give and make system agnostic ( compatible with many types of platform or operating system.)

def get_template_path(path):
        file_path=os.path.join(os.getcwd(),path)
        if not os.path.isfile(file_path):
             raise Exception("This is not a valid template path")
        return file_path


def get_template(path):
    file_path=get_template_path(path)
    return open(file_path).read()


def render_context(template_string,context):
    return template_string.format(**context)

file_='templates/email_message.txt'
template = get_template(file_)
context = {
      'name':'prakhar',
      'date':None,
      'total':None
   }   

print(render_context(template,context))
