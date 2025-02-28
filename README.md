## PRTIMES - チーム 2 - バックエンド

### 開発ルール

開発系は dev/{topic}, 修正は fix/{topic}のような名前のブランチを必ず main ブランチから作成して、作業を行ってください。
また、定期的に origin/main で rebase して最新のコードに追従するようにしてください。

リベースのやり方

```shell
git rebase origin/main
```

また、PR ではテンプレートを作成したので、それを埋める形で情報を記述して、お互いにレビューし合うことにします。

### デプロイ

フロントエンド : cloudflare pages
バックエンド : render
OGP 用サーバー: cloudflare workers

### モックサーバーの起動の仕方

```shell
cd mock
docker compose up --build
```

openapi.yaml に書いてある

```yaml
servers: # base endpoint
  - url: http://localhost:5000/api/v1
    description: base endpoint.
```

の部分は反映されないっぽいので、http://localhost:5000/ から各 API にアクセスしてください。

### サーバーの起動の仕方

```shell
docker compose up -d --build
```

### データベース設計

https://dbdiagram.io/d/67beb268263d6cf9a07c2cbc

### API の設計について(openapi)

https://prtimes-hackathon-2025-winter-team2.github.io/backend/swagger/
