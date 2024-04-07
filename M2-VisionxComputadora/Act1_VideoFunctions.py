import cv2


# Grabación de video
cap1 = cv2.VideoCapture(0)
width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer_normal = cv2.VideoWriter('NormalVideo.mp4',cv2.VideoWriter_fourcc(*'mp4v'),20, (width,height))

while True:
    ret, frame = cap1.read()
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
    writer_normal.write(frame)
    cv2.imshow('frame', frame)

cap1.release()
writer_normal.release()
cv2.destroyAllWindows() 


# Video en Reversa 

cap2 = cv2.VideoCapture("NormalVideo.mp4")
writer_reverse = cv2.VideoWriter('ReverseVideo.mp4',cv2.VideoWriter_fourcc(*'mp4v'),20, (width,height))

check, vid = cap2.read()
frame_list_NV = []

while (check == True):
    check, vid = cap2.read()
    frame_list_NV.append(vid)
frame_list_NV.pop()
frame_list_NV.reverse()

for frame in frame_list_NV:
    cv2.imshow("Frame", frame)
    writer_reverse.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


cap2.release()
writer_reverse.release()
cv2.destroyAllWindows() 

# Juntar videos 
cap3 = cv2.VideoCapture("NormalVideo.mp4")
cap4 = cv2.VideoCapture("ReverseVideo.mp4")
writer_merge = cv2.VideoWriter('MergeVideo.mp4',cv2.VideoWriter_fourcc(*'mp4v'),20, (width,height))

check, vid = cap3.read()
check, vid = cap4.read()
frame_list_NV = []
frame_list_RV = []
frame_list_MV = []

while (check == True):
    check, vid = cap3.read()
    frame_list_NV.append(vid)
    check, vid = cap4.read()
    frame_list_RV.append(vid)

    frame_list_MV = frame_list_NV + frame_list_RV 

for frame in frame_list_MV:
    cv2.imshow("Frame", frame)
    writer_merge.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


cap3.release()
cap4.release()
writer_merge.release()
cv2.destroyAllWindows() 