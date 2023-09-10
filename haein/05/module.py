# 모듈 불러오기 
import os 
import sys 

sys.path

sys.path.append 

'''
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
'''

# echo.py
def echo_test():
    print("echo")
    
# render.py
def render_test():
    print("render")
    
# import game.sound.echo 
# game.sound.echo.echo_test()

# from ..sound.echo import echo_test