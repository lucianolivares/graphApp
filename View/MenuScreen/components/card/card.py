from kivymd.uix.card import MDCard
from kivy.properties import StringProperty


class MenuCard(MDCard):
    image = StringProperty()
    title = StringProperty()