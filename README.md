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
- 名前と年齢の入力チェックを追加

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

- 名前をダイアログで入力
- 名前が空なら再入力
- 年齢をダイアログで入力
- 年齢が不正（空文字/負数/数字以外）なら再入力
- 正常入力時に「来年の年齢」を表示
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
- 名前が空の場合は再入力するように改善
- 年齢が不正（空文字/負数/数字以外）の場合は再入力するように改善
- Git 初期化、初回コミット、GitHub への push を実施
