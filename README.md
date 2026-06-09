# Coffee Log API

コーヒー抽出ログを記録するためのFastAPI学習用アプリです。

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
- Uvicorn

## 起動方法
```bash
./.venv/Scripts/python.exe -m uvicorn main:app --reload
```
## 今後の追加予定
- GET /logs の追加
- GET /logs/{id} の追加
- ログの保存処理の実装
