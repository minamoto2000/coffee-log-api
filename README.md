# Coffee Log API

コーヒー抽出ログを記録するためのFastAPI学習用アプリです。

## 現在できること
- FastAPIの起動確認
- GET / で疎通確認
- POST /logs でログデータの受け取りとバリデーション

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
