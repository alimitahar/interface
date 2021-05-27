#!/usr/bin/env python
# coding: utf-8

# In[5]:


from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win64':
    base = None


executables = [Executable("interface.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)


# In[ ]:





# In[ ]:




