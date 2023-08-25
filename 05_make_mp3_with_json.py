import os
import json
from tkinter import Tk, filedialog
from gtts import gTTS

# スクリプトのあるディレクトリに移動
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Text to speech function
def text_to_speech(text, language, filename):
    text2speech = gTTS(text, lang=language)
    text2speech.save(filename + ".mp3")
    return True

# Tkinterでファイルダイアログを開く
root = Tk()
root.withdraw()  # 主ウィンドウを非表示にする
json_filename = filedialog.askopenfilename(title="Select a JSON file", filetypes=[("JSON files", "*.json")])

# ファイルが選択されたか確認
if json_filename:
    # JSONデータの読み込み
    with open(json_filename, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    # 'contents'内の各'paragraph'から'description'を取得して音声に変換
    if 'contents' in json_data:
        for content in json_data['contents']:
            content_name = content.get('name', '')
            if 'paragraph' in content:
                for paragraph in content['paragraph']:
                    paragraph_name = paragraph.get('name', '')
                    description = paragraph.get('description', '')
                    if description:
                        filename = f"{content_name}_{paragraph_name}"
                        text_to_speech(description, 'en', filename)  # 'ja'は日本語を意味する
                        paragraph['audio'] = filename + ".mp3"

    # 更新されたJSONデータを上書き保存
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
else:
    print("No file selected.")
