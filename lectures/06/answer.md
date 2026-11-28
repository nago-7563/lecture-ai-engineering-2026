# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'topics': ['general'], 'search_phrase': 'Amazon S3 バージョニング 概要'})、aws_aws___search_documentation({'topics': ['general'], 'search_phrase': '"Versioning" bucket same key multiple variants Amazon S3'})
- 気づき・疑問：STEP 2 の回答にあった採点はしないという説明は、trace では途中で切れていて見えなかったが、search_glossary を直接実行すると用語集の定義に書かれていた。STEP 4 では最初の日本語の検索で関係の薄い結果が返り、モデルが英語で検索し直して正しいページにたどり着いた。入力トークンは STEP 2 が715、STEP 3 が2,230、STEP 4 が11,837と増えた。AWS のツールは5個あり説明文も長いので、それが毎回の入力に入ることも一因だと思う。

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル：基礎 / 実装 / 発展
- やったこと：
- 結果：
- 気づき・疑問：
