import pyxel

class App:
    def __init__(self):
        #画面サイズの設定　captionはwindow枠にtext出せる
        pyxel.init(160, 120, caption="Hello Pysel")
        #editorデータ読み込み(コードと同じフォルダにある)
        pyxel.load("my_resource.pyxres")
        #初期化
        self.x = 0
        #実行開始 更新関数 描画関数
        pyxel.run(self.update, self.draw)

    def update(self):
        #右に移動するだけ
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        #画面クリア 0は黒
        pyxel.cls(0)
        #editorデータ描画
        pyxel.blt(self.x, 0, 0, 0, 0, 16, 16, 0)
            #描画座標(左上のX座標)
            #描画座標(左上のY座標)
            #画像番号
            #切り出しの左上のX座標
            #切り出しの左上のY座標
            #切り出す幅
            #切り出す高さ
            #抜き色(パレット番号)

App()
