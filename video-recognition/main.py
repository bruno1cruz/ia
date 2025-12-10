import cv2
import numpy as np
from deepface import DeepFace
from collections import Counter, deque
from tqdm import tqdm
import os
import mediapipe as mp

mp_pose = mp.solutions.pose

def movement_score(landmarks, prev_landmarks):
    # Calculate average movement of keypoints between frames
    if prev_landmarks is None:
        return 0
    score = 0
    for i in range(len(landmarks)):
        dx = landmarks[i].x - prev_landmarks[i].x
        dy = landmarks[i].y - prev_landmarks[i].y
        score += np.sqrt(dx**2 + dy**2)
    return score / len(landmarks)

def infer_activity(landmarks, movement, movement_history):
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
    right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]

    # Standing
    if abs(left_shoulder.y - left_hip.y) > 0.2 and abs(right_shoulder.y - right_hip.y) > 0.2:
        if left_wrist.y > left_shoulder.y and right_wrist.y > right_shoulder.y:
            if movement < 0.01:
                return "standing"
            elif movement > 0.03 and np.mean(movement_history) > 0.03:
                return "walking"
        elif left_wrist.y < left_shoulder.y or right_wrist.y < right_shoulder.y:
            if movement > 0.04 and np.mean(movement_history) > 0.04:
                return "dancing"
            return "raising arm"
    # Sitting
    if abs(left_shoulder.y - left_hip.y) < 0.1 and abs(right_shoulder.y - right_hip.y) < 0.1:
        return "sitting"
    # Dancing: high movement of wrists and ankles
    if movement > 0.05 and np.mean(movement_history) > 0.05:
        return "dancing"
    return "unknown"

def detect_activities_and_emotions(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    activities_summary = []
    emotions_summary = []
    prev_landmarks = None
    movement_history = deque(maxlen=10)

    with mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5) as pose:
        for _ in tqdm(range(total_frames), desc="Processando vídeo"):
            ret, frame = cap.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb_frame)
            activity = "no person"
            movement = 0

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark
                movement = movement_score(landmarks, prev_landmarks)
                movement_history.append(movement)
                activity = infer_activity(landmarks, movement, movement_history)
                mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                prev_landmarks = landmarks
            else:
                movement_history.append(0)
                prev_landmarks = None

            activities_summary.append(activity)

            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                if isinstance(result, list):
                    faces_list = result
                else:
                    faces_list = [result]
                for face in faces_list:
                    x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
                    dominant_emotion = face['dominant_emotion']
                    emotions_summary.append(dominant_emotion)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, dominant_emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
            except Exception as e:
                print(f"Erro ao analisar frame: {e}")

            out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print("Resumo de Atividades:", Counter(activities_summary))
    print("Resumo de Emoções:", Counter(emotions_summary))

# Caminho para o arquivo de vídeo na mesma pasta do script
script_dir = os.path.dirname(os.path.abspath(__file__))
input_video_path = os.path.join(script_dir, 'video.mp4')  # Nome do seu vídeo
output_video_path = os.path.join(script_dir, 'output.mp4')  # Nome do vídeo de saída

# Chamar a função para detectar atividades e emoções no vídeo e salvar o vídeo processado
detect_activities_and_emotions(input_video_path, output_video_path)