# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossary({'query': '3レベル'})
- STEP 3 の [tool call]：fetch_fetch({'url': 'https://modelcontextprotocol.io/'})
- STEP 4 の [tool call]：aws_aws___search_documentation({'topics': ['general'], 'search_phrase': 'Amazon S3 バージョニング 概要'})、aws_aws___search_documentation({'topics': ['general'], 'search_phrase': '"Versioning" bucket same key multiple variants Amazon S3'})
- 気づき・疑問：STEP 2 の回答にあった採点はしないという説明は、trace では途中で切れていて見えなかったが、search_glossary を直接実行すると用語集の定義に書かれていた。STEP 4 では最初の日本語の検索で関係の薄い結果が返り、モデルが英語で検索し直して正しいページにたどり着いた。入力トークンは STEP 2 が715、STEP 3 が2,230、STEP 4 が11,837と増えた。AWS のツールは5個あり説明文も長いので、それが毎回の入力に入ることも一因だと思う。

## 宿題

- 取り組んだレベル：実装
- やったこと：第3回で作った make_quiz を app/mcp_server.py で公開し、範囲外の回を渡されたときの返し方を3通り比べた。A はメッセージを return、B は同じメッセージで ValueError を raise、C は ToolError を raise する。ツール名と説明文はそろえ、用語集に用語がない第5回のクイズを頼んだ。
- 結果：
  - A で第99回を聞いたときはツールが呼ばれず、モデルは第1回から第N回までという曖昧な案内をした。
  - 第5回では3通りともツールが呼ばれ、呼び直しはなかった。
  - A は [tool return] でメッセージが届き、用語がある第1〜4回と第6回を案内できた。
  - B は [tool error] に Error executing tool make_quiz とだけ出て、メッセージは届かなかった。回答は問題を作成しますと言いながら作れず、用語がある回も案内しなかった。
  - C は [tool error] にメッセージ付きで届き、A と同じ案内ができた。
- 気づき・疑問：raise すればメッセージも伝わると思っていたが、普通の例外ではモデルに届かなかった。ログに出た SDK のコメントを見ると、予期しない例外の文はサーバーの外に出さない作りになっていた。モデルに伝えたい説明は return か ToolError で返す必要がある。また第99回のように明らかに範囲外だと、ツールが呼ばれず用意したメッセージが使われないこともあった。
