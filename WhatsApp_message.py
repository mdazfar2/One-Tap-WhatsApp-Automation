#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import pandas as pd

message = '''
"Hello {name}, Are you excited for the Ansible Session?"
'''

def send_message(name, number):
    global message
    if not (name or number):
        return "Number NaN"
    if "+" == number[0]:
        if ('9' == number[1] and '1' == number[2]) or ('1' == number[1]):
            number = number[1:]
    elif ('1' == number[0]):
        number = number[:]
    else:
        number = "91" + number[:]
    print(name, number)
    command = "npx mudslide send {number} ".format(number=number) +  message.format(name=name).strip()
    print(command)
    os.system(command)

if __name__ == "__main__":
    file_path = input('csv file path: ')
    file = pd.read_csv(file_path)
    print(file)
    print(file.columns)
    contacts = file[["Name of the Attendee", "WhatsApp No"]]
    print(contacts)
    for i in range(len(contacts)):
        send_message(contacts['Name of the Attendee'][i].split()[0], str(contacts['WhatsApp No'][i]).rstrip('.0'))


# In[ ]:




