______________________________________________________________________________________________

The Brite Project :Dataset creation from google images- Thales -Mitacs
______________________________________________________________________________________________

Problem : 
To create a quick dataset for testing , it is handy to use google images ,  this projects aims to collect images from google image search,renames and label them to create a dataset to train your convolutional neural network.


EXAMPLE: to create a dataset of road speed limit signs , a search array like the following must be created :        
                 ['canadian road speed limit sign',
                 'spped limit sign canada streets ',
                 'panneaux limite vitesse canada ',
                 'speed limit canada ',
                 'max speed signs canada',
                 'canadian  speed limit signs ',
                 'american  speed limit signs ',
                 'north american speed limit road signs ',
                 'north american speed limit traffic signs '
                  ]

1 - collect_data.py uses serpwow API to download images corresponding to each search sentence, and saves them in different folders.

2 - rename.py renames all the images , it gives a unique name to each image and collects all the images in one folder

3 - Use annotation.py to label the dataset. ( YOLOv2 uses XML files for annotation however YOLOV3 uses txt files instead , use a different annotation tool if using YOLOv3)
