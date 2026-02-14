import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.withdraw()

while True:
    name = simpledialog.askstring("入力", "あなたの名前は？")
    if name is None:
        root.destroy()
        raise SystemExit

    name = name.strip()
    if name:
        break

    messagebox.showerror("エラー", "名前は空で入力できません。")

while True:
    age_text = simpledialog.askstring("入力", "あなたの年齢は？")
    if age_text is None:
        root.destroy()
        raise SystemExit

    age_text = age_text.strip()

    if not age_text:
        messagebox.showerror("エラー", "年齢は空で入力できません。")
        continue

    if age_text.startswith("-") and age_text[1:].isdigit():
        messagebox.showerror("エラー", "年齢は0以上で入力してください。")
        continue

    if age_text.isdigit():
        age = int(age_text)
        break

    messagebox.showerror("エラー", "年齢は数字で入力してください。")

messagebox.showinfo("結果", f"{name}さん、こんにちは！\n来年は {age + 1} 歳ですね。")

root.destroy()
