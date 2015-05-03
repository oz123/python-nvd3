

 * each cell run in python notebook
    has it's last outout saved in `_`.
 
    This could be usefull for asserting that the content is correct. 

 * \ipython nbconvert --to=html --ExecutePreprocessor.enabled=True examples/ipythonDemo.ipynb 
    
    We can then output all cells non-interactively and again make assertion on the HTML generated.

 * one could also use python-nosejs to test , but that project seems abandoned...
   https://pypi.python.org/pypi/NoseJS
