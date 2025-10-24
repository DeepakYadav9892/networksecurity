'''
The setup.py file is an essential part of packaging and distributing 
python porjects.It is used by setuptools (or distutils in older python versionn)
to define the configuration of your project , such as its meta data 
, dependencies and more 
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements 
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ##Read line form the file 
            lines=file.readlines()
            ##Process each line 
            for line in lines:
                requirement=line.strip()
                ##ingnore the empty line and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file not found")

    return requirement_lst
setup(
    name="Networksecurity",
    version="0.0.1",
    author="DeepakYadav",
    packages=find_packages(),
    install_requires=get_requirements()
  )

                     

