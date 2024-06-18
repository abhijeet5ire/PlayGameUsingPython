import mediapipe as mp 
import numpy as np 
import cv2
import pyautogui

#d - defend
#p - punch

cap = cv2.VideoCapture(0)

pose = mp.solutions.pose 
drawing = mp.solutions.drawing_utils
obj = pose.Pose()

space_down=False
w_down=False

while True:
	_, frm = cap.read()

	res = obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

	drawing.draw_landmarks(frm, res.pose_landmarks, pose.POSE_CONNECTIONS)

	if res.pose_landmarks and res.pose_landmarks.landmark[16].visibility > 0.7:
		x = abs(res.pose_landmarks.landmark[16].x * 640 - res.pose_landmarks.landmark[12].x * 640)
		if x > 90:
			print("Punch and Kick Combination")
			if not space_down:
				pyautogui.keyDown("space")
				pyautogui.keyUp("space")
				pyautogui.keyDown("space")
				pyautogui.keyUp("space")
				pyautogui.keyDown("space")
				pyautogui.keyUp("space")
				space_down = True
		else:
			if space_down:
				space_down = False

		if res.pose_landmarks.landmark[16].y * 640 < res.pose_landmarks.landmark[10].y * 640:
			print("Defence")
			if not w_down:
				pyautogui.keyDown("w")
				w_down = True
		else:
			if w_down:
				pyautogui.keyUp("w")
				w_down = False

	frm = cv2.flip(frm, 1)
	cv2.imshow("window", frm)

	if cv2.waitKey(1) == 27:
		cv2.destroyAllWindows()
		cap.release()
		break