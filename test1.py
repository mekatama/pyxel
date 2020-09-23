import pyxel

class App:
    def __init__(self):
        #画面サイズの設定　captionはwindow枠にtext出せる
        pyxel.init(160, 120, caption="Hello Pysel")
        #初期化
        self.x = 0
        #実行開始 更新関数 描画関数
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        #画面クリア 0は黒
        pyxel.cls(0)
        #矩形描画
        pyxel.rect(self.x, 0, 8, 8, 9)

App()
