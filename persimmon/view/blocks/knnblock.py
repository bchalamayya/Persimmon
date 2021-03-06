from persimmon.view.blocks import Block
from persimmon.view.pins import OutputPin

from kivy.properties import ObjectProperty
from kivy.lang import Builder

from sklearn.neighbors import KNeighborsClassifier


Builder.load_file('view/blocks/knnblock.kv')

class KNNBlock(Block):
    est_out = ObjectProperty()

    def function(self):
        self.est_out.val = KNeighborsClassifier()
