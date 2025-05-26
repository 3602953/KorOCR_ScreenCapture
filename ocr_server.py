# ocr_server.py
# 后台常驻OCR服务器
# 按F17键启动
from flask import Flask, request, jsonify
from paddleocr import PaddleOCR
import pyperclip
import subprocess
import os

app = Flask(__name__)
ocr = PaddleOCR(use_angle_cls=True, lang='korean', ocr_version='PP-OCRv4')

# 顯示系統通知（macOS）
def show_notification(message):
    message = message.replace('"', '\\"')  # 转义双引号
    applescript = f'display notification "{message}" with title "识别完成"'
    subprocess.run(["osascript", "-e", applescript])

@app.route('/ocr', methods=['POST'])
def recognize_korean_subtitle():
    image_path = request.form.get('image_path')
    if not image_path or not os.path.exists(image_path):
        show_notification("路径无效或图像不存在")
        return jsonify({'error': '无效的图像路径'}), 400

    result = ocr.ocr(image_path, cls=True)
    if result is None:
        show_notification("OCR识别失败")
        return jsonify({'error': 'OCR识别失败'}), 500

    extracted_text = ""
    for line in result:
        if line:
            for box in line:
                if box:
                    text, confidence = box[1]
                    if float(confidence) > 0.3:
                        extracted_text += text + " "
    extracted_text = extracted_text.strip()

    if extracted_text:
        pyperclip.copy(extracted_text)
        show_notification(extracted_text[:50])  # 显示前50个字符
        return jsonify({'text': extracted_text})
    else:
        show_notification("未识别到字幕，请调整截图范围")
        return jsonify({'text': ''})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
