to run this web application do following steps
1. open command prompt in same directory where you kept requirements.txt file.
2. make a virtual environment using following
        ->  python -m venv .\  
this will create virtual env in current directory 
if this doesn't work use python3 instead of python in command
3. activate virtual environment using following command
	->  .\Scripts\activate	
this will activate virtual env 
4. Now use following command to install all required libraries from requirements.txt 
	->  pip install -r requirements.txt
or	->  pip3 install -r requirements.txt
and wait for all requirements to get installed 
5. To run program now type 
	->  streamlit run main.py 
  