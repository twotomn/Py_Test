# Py_Test

Python学習用のメモです。

## ここまでの実施手順

1. Pythonバージョン確認

```bash
python3 --version
```

2. 仮想環境を作成

```bash
python3 -m venv .venv
```

3. 仮想環境を有効化

```bash
source .venv/bin/activate
```

4. 仮想環境のPythonを確認

```bash
which python
```

5. サンプルコード作成からGUI版へ変更
- 最初は `print("Hello, Python!")`
- その後 `tkinter` を使ったダイアログ入力に変更
- 年齢入力チェックと生年計算を追加

6. Git管理開始

```bash
git init
git add .gitignore README.md main.py
git commit -m "Add initial Python practice app"
```

7. GitHubへpush

```bash
git remote add origin https://github.com/twotomn/Py_Test.git
git push -u origin main
```

## 現在の機能（main.py）

- 年齢をダイアログで入力
- 年齢が不正（空文字/負数/数字以外）なら再入力
- 「今年の誕生日は過ぎましたか？」を `はい/いいえ` で確認
- `いいえ` の場合は生年計算を1年補正
- 結果を `あなたの生まれた年は` の次行に
  `1964年（昭和39年）` 形式で表示
- キャンセル時は終了

## 実行方法

```bash
source .venv/bin/activate
python main.py
```

## 学習ログ

### 2026-02-14

- 空フォルダから Python 学習プロジェクトを開始
- `python3 -m venv .venv` で仮想環境を作成
- `source .venv/bin/activate` で有効化し、`which python` で確認
- `main.py` を作成して CUI の `print` から開始
- `input()` を使った入力処理を実装
- `tkinter` のダイアログ入力へ移行
- 名前と年齢の入力チェックを改善
- 生まれ年を西暦/和暦で表示する機能を追加
- 誕生日が未到来の場合の1年補正を追加
- 表示文言と改行位置を調整
- Git 初期化、コミット、GitHub への push を実施
