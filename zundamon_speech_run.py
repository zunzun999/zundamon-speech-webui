import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))

project_dir = os.path.join(current_dir, "GPT-SoVITS")
os.chdir(project_dir)

streamlit_file = os.path.join(project_dir, "zundamon_webui.py")
subprocess.run(f"streamlit run {streamlit_file}", shell=True)
