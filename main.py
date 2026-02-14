from datetime import date
import tkinter as tk
from tkinter import messagebox, simpledialog


def to_japanese_era(year: int) -> str:
    eras = [
        (2019, "令和"),
        (1989, "平成"),
        (1926, "昭和"),
        (1912, "大正"),
        (1868, "明治"),
    ]

    for start_year, era_name in eras:
        if year >= start_year:
            era_year = year - start_year + 1
            return f"{era_name} {era_year}年"

    return "対象外"


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

passed_birthday = messagebox.askyesno("確認", "今年の誕生日は過ぎましたか？")

birth_year = date.today().year - age
if not passed_birthday:
    birth_year -= 1

japanese_era = to_japanese_era(birth_year)

result_text = (
    f"{name}さんの生まれた年は\n"
#    "生まれた年：\n"
    f"  西暦 {birth_year}年\n"
    f"  和暦 {japanese_era}"
)

messagebox.showinfo("結果", result_text)

root.destroy()
