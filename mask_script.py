"""
make mask files with identical file names and file structure to original files
"""
import os
from PIL import Image, ImageDraw
import shutil


def make_mask(img_width, img_height):
    # make mask
    mask = Image.new('1', size=(img_width, img_height), color=0)
    draw = ImageDraw.Draw(mask)
    center_width = img_width/2
    center_height = img_height/2
    radius = img_height/2
    draw.ellipse((center_width-radius, center_height-radius, center_width+radius, center_height+radius), fill=255)
    return mask

def make_masks(filepath):
    # where we are getting the files
    imgs_filepath = filepath+"/Frames"
    filenames = os.listdir(imgs_filepath)
    
    # get dimensions of target images
    os.chdir(imgs_filepath)
    img = Image.open(filenames[0]) # assuming that all the imgs in a folder are the same dimensions
    img_width = img.width
    img_height = img.height

    # where we want the files to go
    masks_filepath = filepath+"/Masks"

    if os.path.exists(masks_filepath):
        shutil.rmtree(masks_filepath)
    os.mkdir(masks_filepath)

    os.chdir(masks_filepath)

    for jpg_name in filenames:
        if jpg_name.find(".jpg") != -1:
            mask = make_mask(img_width, img_height)
            png_name = jpg_name[:len(jpg_name)-4]+".png"
            # print(png_name)
            mask = mask.save(png_name)

def main():
    endoSLAM_filepath = "/Users/jackieluke/Documents/Brown Fall 2022/ENGN_1610/final_project/endoSLAM"
    os.chdir(endoSLAM_filepath)
    os.chdir("Cameras")

    # camera_names = os.listdir()
    # print(camera_names)

    camera_names = ['HighCam', 'LowCam']
    for camera in camera_names:
        print(camera)
        if camera.find(".") == -1:
            os.chdir(camera)
            organs = os.listdir()
            print(organs)
            for organ in organs:
                if organ != "Calibration" and organ.find(".") == -1:
                    print(organ)
                    os.chdir(organ)
                    trials = os.listdir()
                    print(trials)
                    for trial in trials:
                        if trial.find(".") == -1:
                            print(trial)
                            filepath = endoSLAM_filepath+"/Cameras/"+camera+"/"+organ+"/"+trial
                            make_masks(filepath)
                filepath = endoSLAM_filepath+"/Cameras/"+camera
                os.chdir(filepath)
            filepath = endoSLAM_filepath+"/Cameras/"
            os.chdir(filepath)
            
        
if __name__ == "__main__":
    main()