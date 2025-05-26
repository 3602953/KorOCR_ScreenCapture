#!/bin/bash
# 按F16键截图并上传到OCR服务器
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
IMG_PATH="$(python3 -c 'from config import DEFAULT_CONFIG; print(DEFAULT_CONFIG["IMAGE_DIR"])')/${TIMESTAMP}.png"

/usr/sbin/screencapture -i "$IMG_PATH"

if [ -f "$IMG_PATH" ]; then
  curl -s -X POST -F "image_path=$IMG_PATH" http://127.0.0.1:5000/ocr > /dev/null
else
  /usr/bin/osascript -e 'display notification "截图取消或失败" with title "识别失败"'
fi
