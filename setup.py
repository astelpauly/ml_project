from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
#retrieve libraries as list
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements /libraries
    '''
    #stores name of libraries
    requirements=[]
    #file_obj - temporary object
    with open(file_path) as file_obj:
        #replace \n with blank space
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

#metadata of our project
setup(
    name="ml_project",
    version="0.01",
    author="Astel",
    author_email="astelpauly2002@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)