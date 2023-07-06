import PySimpleGUI as sg
import numpy as np
import cv2


layout = [
    [   
        sg.Button(button_text = "", key = "sapphire_bracelet", tooltip = "Sapphire Bracelet", image_source="Money_Making\Jewelry\images\sapphire_bracelet_100px.png"),
        sg.Button(button_text = "", key = "sapphire_necklace", tooltip = "Sapphire Necklace", image_source="Money_Making\Jewelry\images\sapphire_necklace_100px.png"),
        sg.Button(button_text = "", key = "sapphire_ring", tooltip = "Sapphire Ring", image_source="Money_Making\Jewelry\images\sapphire_ring_100px.png"),
        sg.Button(button_text = "", key = "emerald_bracelet", tooltip = "Emerald Bracelet", image_source="Money_Making\Jewelry\images\emerald_bracelet_100px.png"),
        sg.Button(button_text = "", key = "emerald_necklace", tooltip = "Emerald Necklace", image_source="Money_Making\Jewelry\images\emerald_necklace_100px.png"),
        sg.Button(button_text = "", key = "emerald_ring", tooltip = "Emerald Ring", image_source="Money_Making\Jewelry\images\emerald_ring_100px.png"),
        sg.Button(button_text = "", key = "ruby_bracelet", tooltip = "Ruby Bracelet", image_source="Money_Making/Jewelry/images/ruby_bracelet_100px.png"),
        sg.Button(button_text = "", key = "ruby_necklace", tooltip = "Ruby Necklace", image_source="Money_Making/Jewelry/images/ruby_necklace_100px.png"),
        sg.Button(button_text = "", key = "ruby_ring", tooltip = "Ruby Ring", image_source="Money_Making/Jewelry/images/ruby_ring_100px.png")
    ]
]

window = sg.Window("Jewelry Crafting - Edgeville", layout)


while True:
    event, values = window.read()
    if event == "emerald_bracelet":
        print("emerald bracelet")
        window.close()
    if event == "emerald_necklace":
        print("emerald pearl necklace")

    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break