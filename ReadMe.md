# このソフトウェアについて

フォトライフの画像を表示する。PythonとPillowとImageMagickで。

# 開発環境

* Linux Mint 17.3 MATE
* Python 3.4.3
* SQLite 3.8.2
* ImageMagick
* Pillow

## Webサービス

http://f.hatena.ne.jp/ytyaru/Hatena%20Blog/rss?page=1

# 準備

## DBを作成する

* [はてなアカウントDBを作る](http://ytyaru.hatenablog.com/entry/2017/06/30/000000)
* [はてなブログDBを作る](http://ytyaru.hatenablog.com/entry/2017/07/01/000000)
    * [はてなAPIで取得したXMLからブログ情報を取得しDBに保存する](http://ytyaru.hatenablog.com/entry/2017/07/04/000000)
* [はてなブログ記事DBを作る](http://ytyaru.hatenablog.com/entry/2017/07/02/000000)
    * [はてなAPIで取得したXMLから記事データを取得しDBに保存する](http://ytyaru.hatenablog.com/entry/2017/07/05/000000)
* [はてなフォトライフDBを作る](http://ytyaru.hatenablog.com/entry/2017/07/03/000000)
    * [Pythonでフォトライフから画像をダウンロードする](http://ytyaru.hatenablog.com/entry/2017/07/10/000000)
    * [Pythonでフォトライフから画像をダウンロードする](http://ytyaru.hatenablog.com/entry/2017/07/11/000000)

## 設定する

DBのパスを指定する。

main.py
```python
if __name__ == '__main__':
    viewer = Viewer(
        path_hatena_photolife_sqlite3 = "resource/201703050713/meta_Hatena.PhotoLife.ytyaru.sqlite3"
    )
    viewer.view()
```

表示したい画像のItemIdを指定する。

```python
image = self.db_photo['Contents'].find_one(ItemId='20160608222919')['Content']
```
`Hatena Blog`フォルダははてなブログから画像をアップロードしたときに配置される画像を含んだフォルダである。

# 実行

```sh
python3 main.py
```

# 結果

フォトライフDBのBLOB型列にある画像データがディスプレイに表示される。

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

なお、使用させていただいたライブラリは以下のライセンスである。感謝。

Library|License|Copyright
-------|-------|---------
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[Pillow](https://pillow.readthedocs.io/en/4.0.x/)|[PIL License](https://raw.githubusercontent.com/python-pillow/Pillow/master/LICENSE)|Copyright © 1997-2011 by Secret Labs AB,Copyright © 1995-2011 by Fredrik Lundh,Copyright © 2010-2017 by Alex Clark and contributors
[ImageMagick](http://imagemagick.org/script/index.php)|[ImageMagick License](https://www.imagemagick.org/script/license.php)|Copyright © 1999-2017 ImageMagick Studio LLC

