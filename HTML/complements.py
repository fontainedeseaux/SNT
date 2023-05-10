######################## rajout gestion fenêtre html ####################
from functools import partial
import ipywidgets as widgets
def actualiser(w1,w2,*args):
    '''w1 et w2 sont un widget textarea et un HTML'''
    w2.value=w1.value

# def tester_du_code_html():
#     l=widgets.Layout(flex='0 1 auto', height='140px', min_height='40px',width='auto')
#     t1=widgets.Textarea(value='',layout=l)
#     t2=widgets.HTML(value='')
#     display(t1,t2)
#     t1.observe(partial(actualiser, t1, t2), names='value')

def tester_du_code_html(hauteur_cadre = 140):
    l=widgets.Layout(flex='0 1 auto', height=f'{hauteur_cadre}px', min_height='40px',width='auto')
    t1=widgets.Textarea(value='',layout=l)
    t2=widgets.HTML(value='')
    display(t1,t2)
    t1.observe(partial(actualiser, t1, t2), names='value')