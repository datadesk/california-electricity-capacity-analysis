import os

data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
input_dir = os.path.join(data_dir, 'input')
download_dir = input_dir
output_dir = os.path.join(data_dir, 'output')

os.path.exists(data_dir) or os.mkdir(data_dir)
os.path.exists(input_dir) or os.mkdir(input_dir)
os.path.exists(output_dir) or os.mkdir(output_dir)