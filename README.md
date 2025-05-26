# 韩文OCR识别工具

这是一个简单的韩文OCR识别工具，可以快速识别屏幕上的韩文文字。

## 功能特点

- 支持韩文OCR识别
- 自动复制识别结果到剪贴板
- 系统通知提示识别结果
- 支持快捷键触发

## 安装要求

- Python 3.7+
- macOS系统
- 安装依赖包：`pip install -r requirements.txt`

## 配置说明

在 `config.py` 中可以自定义以下设置：
- `IMAGE_DIR`: 截图保存路径，默认为用户主目录下的 `OCR/dataset_dir/images`

## 使用方法

### 1. 创建 Automator 应用

#### Server端 Automator
1. 打开 Automator
2. 选择"新建文稿" > "应用程序"
3. 在搜索框中输入"运行 Shell 脚本"
4. 拖入"运行 Shell 脚本"动作
5. 在脚本框中输入：
```bash
cd /path/to/your/project
python ocr_server.py
```
6. 保存为应用程序，例如命名为 "OCR Server"

#### Client端 Automator
1. 打开 Automator
2. 选择"新建文稿" > "应用程序"
3. 在搜索框中输入"运行 Shell 脚本"
4. 拖入"运行 Shell 脚本"动作
5. 在脚本框中输入：
```bash
cd /path/to/your/project
./ocr_client.sh
```
6. 保存为应用程序，例如命名为 "OCR Client"

### 2. 设置快捷键

1. 打开System settings > Accessibility > Keyboard > Keyboard settings > Keyboard Shortcut > Services > General
3. 在右侧列表中展开General，找到刚才创建的两个 Automator 应用
4. 为每个应用设置快捷键：
   - OCR Server: 可以按照喜好设置（本人设置为 F17）
   - OCR Client: 可以按照喜好设置（本人设置为 F16）

### 3. 使用流程

1. 首次使用时，运行 OCR Server 应用启动服务器
2. 需要识别文字时：
   - 按下设置的客户端快捷键（如F16）
   - 用鼠标框选要识别的区域
   - 识别结果会自动复制到剪贴板
   - 系统会显示通知提示识别结果

## 文件说明

- `ocr_server.py`: OCR服务器端代码
- `ocr_client.sh`: 客户端截图脚本
- `requirements.txt`: Python依赖包列表
- `config.py`: 配置文件

## 注意事项

- 确保服务器在运行状态
- 识别结果会自动复制到剪贴板
- 识别结果会通过系统通知显示
- 请确保在 Automator 脚本中使用正确的项目路径
- 可以在 `config.py` 中自定义截图保存路径 