import os
import urllib.request as ulib
import json
from serpwow.google_search_results import GoogleSearchResults

url_a = 'https://www.google.com/search?q={}'
url_b = '&hl=en&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi3rdz2mNDiAhVDhq0KHUHuAW8Q_AUIECgB&biw=1853&bih=949'

url_base = ''.join((url_a, url_b))

headers = {'User-Agent': 'Chrome/41.0.2228.0 Safari/537.36'}




def save_images(links, search_name):
    directory = search_name.replace(' ', '_')
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, link in enumerate(links):
        savepath = os.path.join(directory, '{:06}.jpg'.format(i))
        try:
             ulib.urlretrieve(link, savepath)
             print('saved')
        except:
             print('error')
        


if __name__ == '__main__':
    # search_name = 'fidget kid spinner toys'
    # links = get_links(search_name)
    # save_images(links, search_name)

   
    os.chdir('training_images')

##//////////////////////////////////////////////////////////
## ///////////////  Collecting the images //////////////////
##//////////////////////////////////////////////////////////

    # create the serpwow object, passing in our API key
    serpwow = GoogleSearchResults("D91EDA24")
    # search_names=['yield sign france .jpg',
    #              'yield sign usa .jpg',
    #              'yield sign uk .jpg',
    #              'yield sign .jpg',
    #              'canada yield sign .jpg',
    #              'american yield sign .jpg',
    #              'yield sign canada .jpg',
    #              'canadian yield signs .jpg',
    #              'panneaux cédez le passage .jpg'
    #               ]
    # search_names=['stop sign france ',
    #              'stop sign usa ',
    #              'stop sign uk ',
    #              'stop sign ',
    #              'canada stop sign ',
    #              'american stop sign ',
    #              'stop sign canada ',
    #              'canadian stop signs ',
    #              'paneaux arret quebec '
    #               ]
    search_names=['canadian road speed limit sign',
                 'spped limit sign canada streets ',
                 'panneaux limite vitesse canada ',
                 'speed limit canada ',
                 'max speed signs canada',
                 'canadian  speed limit signs ',
                 'american  speed limit signs ',
                 'north american speed limit road signs ',
                 'north american speed limit traffic signs '
                  ]
    
    for search_name in search_names:
        # set up a dict for the search parameters
        params = {
            "q": search_name,
            "location": "United States",
            "google_domain": "google.com",
            "gl": "us",
            "hl": "en",
            "search_type": "images"
        }
        
        # retrieve the search results as JSON
        result = serpwow.get_json(params)
        #print(json.dumps(result))
        links=[]
        for image in result['image_results']:
            if image['image'][len(image['image'])-3:len(image['image'])]=='jpg':
                print(image['image'][len(image['image'])-3:len(image['image'])])
                links.append(image['image'])
        print(len(links))
        save_images(links,search_name)
    print('Image download done')
##//////////////////////////////////////////////////////////
## /////////  Renaming the images  the images //////////////
##//////////////////////////////////////////////////////////

# after saving the images in different folders , we now move 
# them to one folder and rename them starting from 0 to the 
# total number of the images

    #os.chdir('training_images')
    imdir = 'yield_sign_images'
    if not os.path.isdir(imdir):
        os.mkdir(imdir)

    signs_folders = [folder for folder in os.listdir('.') if ('light' in folder) or ('feu' in folder)]
    n = 0
    for folder in signs_folders:
        #files=os.scandir(folder)
        print(folder)
        for imfile in os.scandir(folder):
            os.rename(imfile.path, os.path.join(imdir, '{:06}.jpg'.format(n)))
            n += 1
            print(n,' saved')
        os.rmdir(folder)
            