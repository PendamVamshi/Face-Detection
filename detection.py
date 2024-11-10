import cv2

print("choose type of detection:\n 1.Frontalface Detection\n 2.Eye Detection\n 3.Smile Detection")
choice=int(input())

if choice==1:
    print("DETECTING THE FRONTAL FACE")
    cascade_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0) # web cam capture
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, 0)
        detections = cascade_classifier.detectMultiScale(gray, scaleFactor=1.3,minNeighbors=5)
        if(len(detections) > 0):
            (x,y,w,h) = detections[0]
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2)

        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


elif choice==2:
    print("DETECTING THE EYE")
    cascade_classifier = cv2.CascadeClassifier('haarcascade_eye.xml')
    cap = cv2.VideoCapture(0) # web cam capture
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, 0)
        detections = cascade_classifier.detectMultiScale(gray, scaleFactor=1.3,minNeighbors=5)
        if(len(detections) > 0):
            (x,y,w,h) = detections[0]
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2)

        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


elif choice==3:
    print("DETECTING THE SMILE")
    cascade_classifier = cv2.CascadeClassifier('haarcascade_smile.xml')
    cap = cv2.VideoCapture(0) # web cam capture
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, 0)
        detections = cascade_classifier.detectMultiScale(gray, scaleFactor=1.3,minNeighbors=5)
        if(len(detections) > 0):
            (x,y,w,h) = detections[0]
            frame = cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2)

        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


else:
    print("ERROR")
    print("Given input is choice is incorrect")
    print("choice should be 1 or 2 or 3")


