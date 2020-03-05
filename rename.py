import os

if __name__ == '__main__':
    os.chdir('training_images')
    imdir = 'output'
    if not os.path.isdir(imdir):
        os.mkdir(imdir)

    signs_folders = [folder for folder in os.listdir('.') if ('stop' in folder) ]
    n = 0
    for folder in signs_folders:
        print(folder)
        #files=os.scandir(folder)
        for imfile in os.scandir(folder):
            os.rename(imfile.path, os.path.join(imdir, 'stop_{:06}.jpg'.format(n)))
            n += 1
            print(n,' saved')
        os.rmdir(folder)