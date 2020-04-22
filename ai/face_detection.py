# -*- coding: utf-8 -*-
"""face_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lf9PCm8gHw4hU3CWb-8nut4U6Z43Q3LL
"""

# !pip install face_recognition

import sys
import face_recognition
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import glob

face_locations = []

video_catpture = cv2.VideoCapture(0)

def main():
  while True:
    # ビデオの単一フレームを取得
    _, frame = video_catpture.read()

    # 顔の位置情報を検索
    face_locations = face_recognition.face_locations(frame)

    # 位置情報の表示
    for (top, right, bottom, left) in face_locations:
      # 顔領域を描画
      cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # 結果をビデオで表示
    cv2.imshow("Video", frame)

    # ESCキーで終了
    if cv2.waitKey(1) == 27:
      break

main()

video_catpture.release()
cv2.destroyAllWindows()