Prerequisite:
-------------
Python 3.7.1;

pip;


How to run script:
------------------
pip install -r requirements.txt;

python binary_reverse.py file1 [file2, …];



How to run tests:
-----------------
Entire module:                  
python -m unittest tests.py

Specific class from module:     
python -m unittest tests.Testing

Particularly each test:         
python -m unittest tests.Testing.test_read_input
python -m unittest tests.Testing.test_length_data_equality
python -m unittest tests.Testing.test_reversed_elements

*Note: Please do not delete sample.bin files as they are used as test data.
