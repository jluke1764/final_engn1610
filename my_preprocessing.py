"""
EndoSLAM dataset post COLMAP --> usable form for Liu et al
"""

from my_converter import *
import os

def generate_converted_files(folder_path):
    # folder path is file that contains cameras.txt, images.txt, points3D.txt
    # e.g. /Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/UnityCam/Stomach/sparse/0
    
    
    # make directory for output
    output_folder_name = "output/_start"
    output_path = folder_path+"/"+output_folder_name
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)

    input_path = folder_path
    convert_sparse_data(input_path, output_path)
    


if __name__ == "__main__":
    # generate_converted_files("/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/Colon-IV_1/sparse/0")
    generate_converted_files("/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/UnityCam/Stomach/sparse/0")
    generate_converted_files("/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/UnityCam/Stomach/sparse/1")



    

