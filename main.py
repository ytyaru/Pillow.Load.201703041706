from PIL import Image
from io import BytesIO
import dataset

class Viewer(object):
    def __init__(self, path_hatena_photolife_sqlite3):
        self.db_photo = dataset.connect('sqlite:///' + path_hatena_photolife_sqlite3)

    def view(self):
        image = self.db_photo['Contents'].find_one(ItemId='20160608222919')['Content']
        i = Image.open(BytesIO(image))
        i.show()
        
if __name__ == '__main__':
    viewer = Viewer(
        path_hatena_photolife_sqlite3 = "resource/201703050713/meta_Hatena.PhotoLife.ytyaru.sqlite3"
    )
    viewer.view()

