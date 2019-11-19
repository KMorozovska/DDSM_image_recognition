import os

DDSM_url = "http://www.eng.usf.edu/cvprg/Mammography/Database.html"

main_dir = os.path.split(os.path.abspath(__file__))[0]

pickles_path = os.path.join(main_dir, "pickles")
images_path = os.path.join(main_dir, "images")
