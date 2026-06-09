# Coffee Log API

コーヒー抽出ログを記録するためのFastAPI学習用APIです。

## 現在できること

- FastAPIでAPIを起動できる
- SQLiteにコーヒーログを保存できる
- GET /logs でログ一覧を取得できる
- GET /logs/{log_id} でログを1件取得できる
- POST /logs でログを作成できる
- PUT /logs/{log_id} で overall_score を更新できる
- DELETE /logs/{log_id} でログを削除できる
- Swagger UI でAPIの動作確認ができる

## 使用技術

- Python
- FastAPI
- Pydantic
- SQLite
- Uvicorn

## 起動方法

```bash
./.venv/Scripts/python.exe -m uvicorn main:app
```

開発中に自動リロードを使う場合は、仮想環境を監視対象から外して起動します。

```bash
./.venv/Scripts/python.exe -m uvicorn main:app --reload --reload-exclude ".venv/*"
```

起動後、Swagger UIでAPIを確認できます。

```text
http://127.0.0.1:8000/docs
```

## API一覧

| Method | Path | 内容 |
| --- | --- | --- |
| GET | /logs | ログ一覧を取得 |
| GET | /logs/{log_id} | 指定したログを1件取得 |
| POST | /logs | ログを作成 |
| PUT | /logs/{log_id} | 指定したログの overall_score を更新 |
| DELETE | /logs/{log_id} | 指定したログを削除 |

## 今後の追加候補

- 入力項目の追加
- エラーハンドリングの整理
- テストの追加
- ファイル分割
