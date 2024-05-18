import cv2
import pyautogui
import numpy as np
import pygetwindow as gw

window_name = "test.txt" #Window name to record, Example: Note.txt (Notepad TXT file)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 30.0 #FPS
record_seconds = 15 #Seconds of record

w = gw.getWindowsWithTitle(window_name)[0] #[0] = Index
w.activate

out = cv2.VideoWriter("output.avi", fourcc, fps, tuple(w.size)) # Build the video

for i in range(int(record_seconds * fps)):
    img = pyautogui.screenshot(region=(w.left, w.top, w.width, w.height))
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("screenshot", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows() #Destroys CV2 window
out.release() #Create video
