# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:10:16 2021

@author: nilsv
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May  4 14:26:37 2021

@author: natho
"""

from fichefonction import placement_bateau 
from fichefonction import placement_ordi

from random import randint
import PySimpleGUI as sg

largeur_case = 8
longueur_bouton=4
tableau = [[0 for i in range(10)] for i in range(10)]
tab =["A","B","C","D","E","F","G","H","I","J"]
tableau1 =[[0 for i in range(10)] for i in range(10)]
positionC= False
positionT1= False
positionT2= False
positionS= False
positionCordi= False
positionT1ordi= False
positionT2ordi= False
positionSordi= False
V= False
V2= False
m=0
n=0
scoreJ1=25
scoreOrdi=25

grille_joueur=[
    [sg.Text('A', pad=(30, 5)),sg.Text('B', pad=(30, 5)),sg.Text('C', pad=(30, 5)),sg.Text('D', pad=(30, 5)),sg.Text('E', pad=(30, 5)),sg.Text('F', pad=(30, 5)),sg.Text('G', pad=(30, 5)),sg.Text('H', pad=(30, 5)),sg.Text('I', pad=(30, 5)),sg.Text('J', pad=(30, 5))],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A1"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B1"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C1"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D1"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E1"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F1"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G1"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H1"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I1"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J1"),sg.Text('1')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A2"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B2"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C2"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D2"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E2"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F2"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G2"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H2"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I2"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J2"),sg.Text('2')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A3"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B3"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C3"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D3"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E3"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F3"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G3"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H3"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I3"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J3"),sg.Text('3')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A4"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B4"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C4"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D4"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E4"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F4"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G4"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H4"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I4"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J4"),sg.Text('4')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A5"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B5"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C5"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D5"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E5"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F5"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G5"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H5"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I5"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J5"),sg.Text('5')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A6"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B6"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C6"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D6"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E6"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F6"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G6"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H6"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I6"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J6"),sg.Text('6')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A7"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B7"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C7"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D7"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E7"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F7"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G7"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H7"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I7"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J7"),sg.Text('7')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A8"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B8"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C8"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D8"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E8"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F8"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G8"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H8"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I8"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J8"),sg.Text('8')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A9"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B9"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C9"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D9"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E9"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F9"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G9"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H9"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I9"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J9"),sg.Text('9')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A10"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B10"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C10"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D10"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E10"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F10"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G10"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H10"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I10"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J10"),sg.Text('10')],
    [sg.Button("Placer"),sg.Button("Commencer")]
    ]
plateau_jeu=[
    [sg.Text('A', pad=(30, 5)),sg.Text('B', pad=(30, 5)),sg.Text('C', pad=(30, 5)),sg.Text('D', pad=(30, 5)),sg.Text('E', pad=(30, 5)),sg.Text('F', pad=(30, 5)),sg.Text('G', pad=(30, 5)),sg.Text('H', pad=(30, 5)),sg.Text('I', pad=(30, 5)),sg.Text('J', pad=(30, 5))],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A1"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B1"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C1"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D1"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E1"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F1"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G1"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H1"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I1"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J1"),sg.Text('1')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A2"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B2"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C2"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D2"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E2"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F2"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G2"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H2"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I2"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J2"),sg.Text('2')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A3"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B3"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C3"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D3"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E3"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F3"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G3"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H3"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I3"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J3"),sg.Text('3')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A4"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B4"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C4"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D4"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E4"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F4"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G4"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H4"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I4"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J4"),sg.Text('4')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A5"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B5"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C5"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D5"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E5"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F5"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G5"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H5"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I5"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J5"),sg.Text('5')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A6"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B6"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C6"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D6"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E6"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F6"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G6"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H6"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I6"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J6"),sg.Text('6')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A7"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B7"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C7"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D7"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E7"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F7"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G7"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H7"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I7"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J7"),sg.Text('7')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A8"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B8"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C8"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D8"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E8"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F8"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G8"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H8"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I8"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J8"),sg.Text('8')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A9"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B9"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C9"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D9"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E9"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F9"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G9"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H9"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I9"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J9"),sg.Text('9')],
    [sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="A10"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="B10"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="C10"),sg.Button("", size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="D10"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="E10"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="F10"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="G10"), sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="H10"),sg.Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="I10"), sg. Button("",size=(largeur_case,longueur_bouton),pad=(0,0),button_color=("#2EFEF7"),key="J10"),sg.Text('10')],
    [sg.Button("Play")]]



window1=sg.Window("plateau de jeu", layout=plateau_jeu)
window=sg.Window("Bataille navale", layout=grille_joueur)

#Plateau de jeu

while True:
    event, values = window.read() 
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Placer':  

#Placement porte-avion
        textetoprint = "Porte-avion: horizontal ou vertical?"
        tableau,window=placement_bateau(5,tab,tableau,window,textetoprint)
       
           
#Placement croiseur
        textetoprint = "croiseur: horizontal ou vertical?"
        tableau,window=placement_bateau(4,tab,tableau,window,textetoprint)
        
     
                
                
#Placement torpilleur1


        textetoprint = "Torpilleur1: horizontal ou vertical?"
        tableau,window=placement_bateau(3,tab,tableau,window,textetoprint)
        
                     
#Placement torpilleur2

        textetoprint = "Torpilleur2: horizontal ou vertical?"
        tableau,window=placement_bateau(3,tab,tableau,window,textetoprint)
        
       
                
#Placement sous-marin

        textetoprint = "Sous-marin: horizontal ou vertical?"
        tableau,window=placement_bateau(2,tab,tableau,window,textetoprint)
       
                        
 #Placement porte-avion Ordi
        tableau1=placement_ordi(5,tab,tableau1)

    #Placement croiseur Ordi
        
        tableau1=placement_ordi(4,tab,tableau1)
       
    #Placement torpilleur1 Ordi
        tableau1=placement_ordi(3,tab,tableau1)
       
    #Placement torpilleur2 Ordi
        tableau1=placement_ordi(3,tab,tableau1)
       
                
    #Placement sous-marin Ordi
    
        tableau1=placement_ordi(2,tab,tableau1)
        
        print("Placement terminé")           
           
                
#Tir                
    elif event=='Commencer':
       
            event, values = window1.read() 
            print(event, values)
            if event == sg.WIN_CLOSED:
               break
            elif event=="Play":
                while V==False and V2==False:    #tant qu'un des deux joueurs n'a pas coulé tous les navires adverses.
                        a=4
                        b=5
                        Tir_touche=True
                        while Tir_touche==True: #assure le tour du joueur tant qu'il touche un navire
                            Tc=str(input("Colonne"))
                            Tl=int(input("Ligne"))
                            g = tab.index(Tc)
                            scoreJ1=scoreJ1-1
                                
                            if  tableau1[Tl-1][g] == 1:  #Il a touché!
                                Tir_touche=True
                                print("Touché!")
                                tableau1[Tl-1][g] = a
                                window1[Tc+str(Tl)].Update(button_color = ('red'))
                                m=m+1
                                scoreJ1=scoreJ1+3
                                window1.read()
                                
                                
                            else:                   #Il a manqué donc le booléen tir_touche est faux et break la boucle --> passe au tour de l'ordi
                                print("Raté!")
                                window1[Tc+str(Tl)].Update(button_color = ('blue')) 
                                tableau1[Tl-1][g] = b
                                window1.read()
                                print("Tour Ordinateur")
                                Tir_touche=False

                            
                            if m>=17 :  #Si m>=17 cela veut dire que le joueur à touché 17fois, il a donc détruit tous les bateaux adverses(5+4+3+3+2=17)
                                V=True 
                                break
                             
                       
                        while Tir_touche==False:
                            scoreOrdi=scoreOrdi-1
                            Tc=int(randint(0,9))
                            Tl=int(randint(0,9))
                            if tableau[Tl][Tc] == a or tableau[Tl][Tc] == b:
                                Tir_touche=False
                                print("Déjà tiré à cet emplacement !")
                                continue
                            print("Tir en ",tab[Tc],Tl)
                            
                            if  tableau[Tl][Tc] == 1:
                                print("Touché!")
                                tableau[Tl][Tc] = a
                                window[tab[Tc]+str(Tl+1)].Update(button_color = ('red'))
                                n=n+1
                                scoreOrdi=scoreOrdi+3
                                
                            else:
                                print("Raté!")
                                window[tab[Tc]+str(Tl+1)].Update(button_color = ('blue'))
                                tableau[Tl-1][g] = b
                                print("C est à votre tour")
                                Tir_touche=True
                                
                            if n>=17 :  # Met fin au jeux si l'ordi gagne
                                V2=True      
                                break  
                if V== True : # Annonce que le gagnant est le joueur 
                    print("VOUS AVEZ GAGNE !! ")
                    print("Vous avez un score de : ",scoreJ1)
                    print(" L'adversaire a un score de :  ",scoreOrdi)
                if V2== True : #Annonce que l'ordi gagne
                    print("VOUS AVEZ PERDU !! ")
                    print("Vous avez un score de : ",scoreJ1)
                    print(" L'adversaire a un score de :  ",scoreOrdi)