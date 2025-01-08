import argparse
import fs


epoch = 946684800 # 2000/01/01 00:00:00 GMT


def sort_psp_games(path='ISO'):
    # The games are sorted by created date of file (cso or iso)
    global epoch, my_fs
    for entry in sorted(my_fs.scandir(path), key=lambda entry: entry.name):
        if entry.is_dir:
            sort_psp_games(f'{path}/{entry.name}')
        elif entry.name.casefold().endswith(('cso', 'iso')):
            print('Sorting', f'{path}/{entry.name}')
            my_fs.setinfo(f'{path}/{entry.name}', {'details':{'created':epoch}})
            epoch -= 60

def sort_psp_apps(path='PSP/GAME'):
    # The apps are sorted by modified date of containing EBOOT.PBP folder
    global epoch, my_fs
    for entry in sorted(my_fs.scandir(path), key=lambda entry: entry.name):
        if entry.is_dir:
            files = my_fs.listdir(f'{path}/{entry.name}')
            if [x for x in files if x.casefold() == 'eboot.pbp']:
                print('Sorting', f'{path}/{entry.name}')
                my_fs.setinfo(f'{path}/{entry.name}', {'details':{'modified':epoch}})
                epoch -= 60
            else:
                sort_psp_apps(f'{path}/{entry.name}')


parser = argparse.ArgumentParser(description='Sort games and apps alphabetically on the Sony PSP')
parser.add_argument(
    'device',
    type=str,
    help='Sony PSP device partition (Example: /dev/sda1)'
)

group = parser.add_mutually_exclusive_group()

group.add_argument(
    '-a',
    '--apps',
    action='store_true',
    help='Sort apps only (ROOT/PSP/GAME dir)'
)
group.add_argument(
    '-g',
    '--games',
    action='store_true',
    help='Sort PSP game ISOs only (ROOT/ISO dir)'
)

args = parser.parse_args()
device = args.device

try:
    with fs.open_fs(f'fat://{device}') as my_fs:
        if args.games:
            sort_psp_games()
        elif args.apps:
            sort_psp_apps()
        else:
            sort_psp_games()
            sort_psp_apps()
except Exception as err:
    print(err)