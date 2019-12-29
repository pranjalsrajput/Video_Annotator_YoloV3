# Video_Annotator_YoloV3

For bounding box and labels based annotation of videos using YoloV3 

1. Clone the repository and install requirements
   cd PyTorch-YOLOv3/
   sudo pip3 install -r requirements.txt
   
2. Put your data in `data/samples/` folder

3. Run `python3 detect.py --image_folder data/samples/`

4. The system will take each image/frame and will ask to either annotate(Press `Continue`) or not(Press `Skip`)?

5. If `Skip` is pressed, then next image/frame will be taken. If `Continue` is pressed then you will be asked to put the `label` value
 (in our case it's bibId of the runners). You can `Enter` a value or `Quit` if don't want to put any label for that object (in this case runner).
 
6. In the end, the annotateed images will be saved in the `output` folder.
