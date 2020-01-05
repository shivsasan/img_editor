
#importing libraries
import sys
import cv2 as cv
import numpy as np
import os


#global variables for keeping track of changes 
edited = 'not yet'
rotCheck = 0
changed = 0
preview = 0

#resize function
def resize(img):

    global edited
    global changed
    #img = input('Enter the name of the image with the extention:\t')
    xscale = float(input('Enter scale factor for x axis:\t'))
    yscale = float(input('Enter scale factor for y axis:\t'))

    #img = cv.imread(img)
    
    resized = cv.resize(img,None,fx = xscale, fy = yscale, interpolation = cv.INTER_LINEAR)
    
    #show the image with changes done to it
    cv.imshow('resized_image',resized)
    cv.waitKey(0)
    cv.destroyAllWindows()

    #ask the user if they want to keep the change or discard
    while True:
        print('Would you like to keep the changes? [y/n]: ')
        decision = input()
        if decision == 'y' or decision == 'Y':
            edited = resized
            changed = 1
            return
        elif decision == 'n' or decision == 'N':
            return
        else:
            print('Wrong input! Retry')
            #check = True

#function to perform 90 degree rotation on the images
def rotation(image):

    global edited
    global rotCheck
    global changed

    print('Select one of the 90 degree rotations:')
    print('1\tClockwise')
    print('2\tCounter Cloackwise')

    while True:
        angle = int(input('Option:\t'))
        if angle != 1 and angle !=2:
            print('Wrong Option! RETRY')
        else:
            break

    #choose angle to rotate depending on the type of rotation
    if angle == 1:
        angle = 270
    if angle == 2:
        angle = 90
    
    l, w = image.shape[0:2]

    #rotCheck is used to check if the image has been rotated once or not and chooses the scale factor accordingly

    if rotCheck == 0:
        rMat = cv.getRotationMatrix2D((w/2,l/2),angle,0.5)
        rotCheck = 1
    elif rotCheck == 1:
        rMat = cv.getRotationMatrix2D((w/2,l/2),angle,2)
        rotCheck = 0

    rotated = cv.warpAffine(image,rMat,(w,l))
    cv.imshow('Rotated Image',rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()

    while True:
        print('Would you like to keep the changes? [y/n]: ')
        decision = input()
        if decision == 'y' or decision == 'Y':
            edited = rotated
            changed = 1
            return
        elif decision == 'n' or decision == 'N':
            return
        else:
            print('Wrong input! Retry')
            #check = True

#function to flip images
def flip(image):
    global edited
    global changed

    print('How would you like to flip the image?: ')
    print('\t1\tFlip Vertically')
    print('\t2\tFlip Horizontally')
    print('\t3\tFlip Horizontally and Vertically')

    while True:
        func = int(input('Option:\t'))
        if func < 1 or func > 3:
            print('Wrong Option! Retry')
        else:
            break
    flippedImage = image

    if func == 1:
        flippedImage = cv.flip(image,0)
    elif func == 2:
        flippedImage = cv.flip(image,1)
    elif func == 3:
        flippedImage = cv.flip(image,-1)
    
    cv.imshow('Flipped Image',flippedImage)
    cv.waitKey(0)
    cv.destroyAllWindows()

    #flag = True
    while True:
        print('Would you like to retain the changes? [y/n]: ')
        decision = input()
        if decision == 'y' or decision == 'Y':
            edited = flippedImage
            changed = 1
            return
        elif decision == 'n' or decision == 'N':
            return
        else:
            print('Wrong input! Retry')
            #check = True

#defination of main function
def main():
    global edited
    '''
    print(len(sys.argv))
    
    if len(sys.argv) > 1:
        a = 0
        while a < len(sys.argv):
            print(sys.argv[a])
            print("\t")
            a = a + 1
        
    '''    
    
    print('Name of the image you would like to edit (with extension): ')

    name = input('Name: ')

    #read the image and convert to matrix
    img = cv.imread(name)
    edited = img

    #show original image
    #cv.imshow('Original image',img)

    #options
    print('What would you like to do:')
    print('\t1\tResize Image')
    print('\t2\tRotate Image')
    print('\t3\tFlip Image')
    print('\t4\tEXIT')

    while True:
        func = int(input('Option:\t'))

        if func < 1 or func > 4:
            print('Wrong integer entry! Please Retry')
        else:
            break
    
    #depending on the value of func, call the appropriate function 
    if func == 1:
        resize(img)
        
    if func == 2:
        rotation(img)

    if func == 3:
        flip(img)
        
    if func == 4:
        print('EXITTING!')
        exit()
    
    #this while loop starts after some editing is performed on the image
    #The program now gives an option to SAVE changes
    while True:

        inpCheck = 1
        while inpCheck:
            print('What would you like to do:')
            print('\t1\tResize')
            print('\t2\tRotate')
            print('\t3\tFlip')
            print('\t4\tSAVE and EXIT')
            print('\t5\tEXIT without saving')

            func = int(input('Option:\t'))
            if func < 1 or func > 5:
                print('Wrong input! Retry')
            else:
                inpCheck = 0

        if func == 1:
            resize(edited)
        if func == 2:
            rotation(edited)
        if func == 3:
            flip(edited)
        if func == 4:
            cv.imwrite('edited.png',edited)
            print('SAVING changes and EXITING')
            exit()
        if func == 5:
            print('Exiting without saving!\nBye')
            exit()
    

if __name__ == "__main__":
    main()