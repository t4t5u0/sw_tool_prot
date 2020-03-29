from swtool import commands
from swtool.color import Color


def process(arg):
    if arg == []:
        return
    elif arg[1:] == [] :
        try:
            eval(f'commands.{arg[0]}()')
        except TypeError as e:
            print(f'{type(e)} {e}')
            print(f'{Color.YELLOW}引数が足りないよ{Color.RESET}')
        except AttributeError as e:
            print(f'{type(e)} {e}')
            print(f'{Color.YELLOW}そんな関数ないよ{Color.RESET}')
        except SyntaxError as e:
            print(f'{type(e)} {e}')
            print(f'{Color.YELLOW}その他エラー{Color.RESET}')
    else:
        try:
            eval(f'commands.{arg[0]}({arg[1:]})')
        except TypeError:
            #print(f'{type(e)} {e}')
            print(f'{Color.YELLOW}引数がおかしいよ{Color.RESET}')
        except AttributeError:
            #print(f'{type(e)} {e}')
            print(f'{Color.YELLOW}そんな関数ないよ{Color.RESET}')
        except SyntaxError as e:
            #print(f'{type(e)} {e}')
            print(f'{Color.YELLOW}その他エラー{Color.RESET}')