from setuptools import find_packages,setup
from typing import List
hypenedot='-e .'
def getrequirement(file_path:str)->List[str]:
    
    
    requirement=[]

    with open(file_path) as file:
        
        requirement=file.readlines()
        requirement=[r.replace('\n',"") for r in requirement]
        if hypenedot in requirement:
            requirement.remove(hypenedot)
        return requirement

setup(
    name='mlproject',
    version='0.0.1',
    author='Sarthak Patel',
    author_email='sarthakgangwar1700@gmail.com',
    packages=find_packages(),
    install_requires=getrequirement('requirement.txt')
    



)