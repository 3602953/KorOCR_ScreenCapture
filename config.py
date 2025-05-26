import os

# 获取用户主目录
HOME_DIR = os.path.expanduser("~")

# 默认配置
DEFAULT_CONFIG = {
    "IMAGE_DIR": os.path.join(HOME_DIR, "OCR", "dataset_dir", "images"),
}

# 确保图片目录存在
os.makedirs(DEFAULT_CONFIG["IMAGE_DIR"], exist_ok=True) 