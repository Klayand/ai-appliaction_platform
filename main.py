import subprocess
import os


def run_streamlit():
    py_process = subprocess.call(['streamlit', 'run',  os.path.abspath(os.path.join(os.getcwd(), '🏠_Home.py'))])

run_streamlit()

