# coding: utf

import os
import datetime
import json
import math
import datetime
import sys
sys.path.append("./vendor")
from pprint import pprint

lambda_tmp_dir = '/tmp'
ffmpeg_bin = "{0}/ffmpeg.linux64".format(lambda_tmp_dir)
os.environ['IMAGEIO_FFMPEG_EXE'] = ffmpeg_bin
from moviepy.editor import *

# settings
one_move_duration = 1
fontsize = 83
one_width = 100
margin_x_left = 200
margin_x_right = 300
margin_y = 100
padding_x = 10
padding_y = 10
screensize = (one_width * 9 + margin_x_left + margin_x_right, one_width * 9 + (margin_y * 2))

def set_init_pos():

    pieces_pos = [
                    {'name':'FU', 'color':0, 'x':9, 'y':7 },
                    {'name':'FU', 'color':0, 'x':8, 'y':7 },
                    {'name':'FU', 'color':0, 'x':7, 'y':7 },
                    {'name':'FU', 'color':0, 'x':6, 'y':7 },
                    {'name':'FU', 'color':0, 'x':5, 'y':7 },
                    {'name':'FU', 'color':0, 'x':4, 'y':7 },
                    {'name':'FU', 'color':0, 'x':3, 'y':7 },
                    {'name':'FU', 'color':0, 'x':2, 'y':7 },
                    {'name':'FU', 'color':0, 'x':1, 'y':7 },
                    {'name':'KA', 'color':0, 'x':8, 'y':8 },
                    {'name':'HI', 'color':0, 'x':2, 'y':8 },
                    {'name':'KY', 'color':0, 'x':9, 'y':9 },
                    {'name':'KE', 'color':0, 'x':8, 'y':9 },
                    {'name':'GI', 'color':0, 'x':7, 'y':9 },
                    {'name':'KI', 'color':0, 'x':6, 'y':9 },
                    {'name':'OU', 'color':0, 'x':5, 'y':9 },
                    {'name':'KI', 'color':0, 'x':4, 'y':9 },
                    {'name':'GI', 'color':0, 'x':3, 'y':9 },
                    {'name':'KE', 'color':0, 'x':2, 'y':9 },
                    {'name':'KY', 'color':0, 'x':1, 'y':9 },
                    {'name':'FU', 'color':1, 'x':9, 'y':3 },
                    {'name':'FU', 'color':1, 'x':8, 'y':3 },
                    {'name':'FU', 'color':1, 'x':7, 'y':3 },
                    {'name':'FU', 'color':1, 'x':6, 'y':3 },
                    {'name':'FU', 'color':1, 'x':5, 'y':3 },
                    {'name':'FU', 'color':1, 'x':4, 'y':3 },
                    {'name':'FU', 'color':1, 'x':3, 'y':3 },
                    {'name':'FU', 'color':1, 'x':2, 'y':3 },
                    {'name':'FU', 'color':1, 'x':1, 'y':3 },
                    {'name':'HI', 'color':1, 'x':8, 'y':2 },
                    {'name':'KA', 'color':1, 'x':2, 'y':2 },
                    {'name':'KY', 'color':1, 'x':9, 'y':1 },
                    {'name':'KE', 'color':1, 'x':8, 'y':1 },
                    {'name':'GI', 'color':1, 'x':7, 'y':1 },
                    {'name':'KI', 'color':1, 'x':6, 'y':1 },
                    {'name':'OU', 'color':1, 'x':5, 'y':1 },
                    {'name':'KI', 'color':1, 'x':4, 'y':1 },
                    {'name':'GI', 'color':1, 'x':3, 'y':1 },
                    {'name':'KE', 'color':1, 'x':2, 'y':1 },
                    {'name':'KY', 'color':1, 'x':1, 'y':1 }
                ]
#    pieces_pos = pd.DataFrame(pieces_pos)
#    pieces_pos.columns.name = 'id'

    return pieces_pos

def switch_promote_name(name, promote = 0):
    promote_pieces = {
                    'FU':'TO',
                    'KY':'NY',
                    'KE':'NK',
                    'GI':'NG',
                    'KA':'UM',
                    'HI':'RY'
                }

    if promote == 1:
        return promote_pieces[name]
    else:
        if name in promote_pieces.values():
            return [k for k, v in promote_pieces.items() if name in v][0]
        else:
            return name

def calc_pos(x, y):
    pos_x = (10 - x) * one_width - one_width + padding_x + margin_x_left
    pos_y = y * one_width - one_width + padding_y + margin_y

    return [pos_x, pos_y]

def calc_hand_pos(color, index, count_flg=False):

    if color == 0:
        count_padding_x = int(one_width * 0.8) if count_flg == True else 0
        count_padding_y = int(one_width / 3) if count_flg == True else 0
        return [(one_width * 9) + margin_x_left + (margin_x_left / 2) + padding_x + count_padding_x, ((index * one_width) + one_width + margin_y + padding_y + count_padding_y)]
    else:
        count_padding_x = one_width / 2 if count_flg == True else 0
        return [(margin_x_left - one_width + padding_x - count_padding_x), ((one_width * 7) + margin_y - (index * one_width) + padding_y)]

def set_move_pos(pos_from_x, pos_from_y, pos_to_x = None, pos_to_y = None):
    if pos_to_x is not None and pos_from_x != pos_to_x:
        if pos_from_x < pos_to_x:
            x = lambda t : min(pos_from_x+(((pos_to_x-pos_from_x)/one_move_duration)*t), pos_to_x)
        else:
            x = lambda t : max(pos_from_x-(((pos_from_x-pos_to_x)/one_move_duration)*t), pos_to_x)
    else:
        x = lambda t : pos_from_x

    if pos_to_y is not None and pos_from_y != pos_to_y:
        if pos_from_y < pos_to_y:
            y = lambda t : min(pos_from_y+(((pos_to_y-pos_from_y)/one_move_duration)*t), pos_to_y)
        else:
            y = lambda t : max(pos_from_y-(((pos_from_y-pos_to_y)/one_move_duration)*t), pos_to_y)
    else:
        y = lambda t : pos_from_y

    return lambda t: (x(t), y(t))

def meke_text_clip(piece, color):
    piece_name = {"FU":"歩", "KY":"香", "KE":"桂", "GI":"銀", "KI":"金", "KA":"角", "HI":"飛", "OU":"王",
                    "TO":"と", "NY":"杏", "NK":"圭", "NG":"全", "UM":"馬", "RY":"龍"}
    text_clip = TextClip(piece_name[piece],color='Black', bg_color='White', font="IPAゴシック-Regular", fontsize=fontsize)

    if color == 1:
        w,h = text_clip.size
        rotated_clip = (text_clip.add_mask()
                        .fx(vfx.resize, width=w, height=h)
                        .fx(vfx.rotate, 180, expand=False)
                        )
        return rotated_clip
    else:
        return text_clip

def meke_count_clip(color, count):
    fontsize = 50
    text_clip = TextClip('x%s' % (count),color='Black', bg_color='White', font="IPAゴシック-Regular", fontsize=fontsize)

    if color == 1:
        w,h = text_clip.size
        rotated_clip = (text_clip.add_mask()
                        .fx(vfx.resize, width=w, height=h)
                        .fx(vfx.rotate, 180, expand=False)
                        )
        return rotated_clip
    else:
        return text_clip

def add_hand_piece(hand_pieces, name, color):
    for k, v in enumerate(hand_pieces[color]):
        if name in v.values():
            hand_pieces[color][k]['count'] = v['count'] + 1
            break
    else:
        hand_pieces[color].append({'name': name, 'color': color, 'count': 1})

def make_clips():
    move_clips = []
    hand_pieces = [[],[]]
    count = 0

    for row in moves:
        if row.get('move'):
            text_clips = []
            print("%s - - - -" % (count))

            if row['move']['from'] is None:
                # uchi
                print("%s) uchi" % (i))
                print(hand_pieces[row['move']['color']])

                # use hand piece
                for k, v in enumerate(hand_pieces[row['move']['color']]):
                    if row['move']['piece'] in v.values():
                        text_clip = meke_text_clip(row['move']['piece'], row['move']['color'])
                        pos_from_x, pos_from_y = calc_pos(row['move']['to']['x'], row['move']['to']['y'])
                        text_clips.append(text_clip.set_pos((pos_from_x, pos_from_y)))
                        del hand_pieces[row['move']['color']][k]
                        pieces_pos.append({'name':row['move']['piece'], 'color':row['move']['color'], 'x':row['move']['to']['x'], 'y':row['move']['to']['y'] })
#                        print(pieces_pos)
                        break
                else:
                    pirnt('Error hand piece nothing!')

            # hand piece
            for j, hand_piece in enumerate(hand_pieces):
                for k, piece in enumerate(hand_piece):
                    pos_from_x, pos_from_y = calc_hand_pos(piece['color'], k)
                    text_clip = meke_text_clip(piece['name'], piece['color'])
                    text_clips.append(text_clip.set_pos((pos_from_x, pos_from_y)))
                    print("%s) hand_piece sente %s %s %s %s" % (k, piece['name'], piece['color'], pos_from_x, pos_from_y))

                    if piece['count'] > 0:
                        pos_from_x, pos_from_y = calc_hand_pos(piece['color'], k, True)
                        text_clip = meke_count_clip(piece['color'], piece['count'])
                        text_clips.append(text_clip.set_pos((pos_from_x, pos_from_y)))

            #for i, piece in pieces_pos.iterrows():
            for i, piece in enumerate(pieces_pos):
                text_clip = meke_text_clip(piece['name'], piece['color'])
                pos_from_x, pos_from_y = calc_pos(piece['x'], piece['y'])

#                text_clips.append(text_clip.set_pos((pos_from_x, pos_from_y)))

                if row['move']['from'] is not None and row['move']['from']['x'] == piece['x'] and row['move']['from']['y'] == piece['y']:
                    # move
                    print("%s) move from %s %s to %s %s" % (i, piece['x'], piece['y'], row['move']['to']['x'], row['move']['to']['y']))

                    # set_pos
                    pos_to_x, pos_to_y = calc_pos(row['move']['to']['x'], row['move']['to']['y'])
                    text_clips.append(text_clip.set_pos(set_move_pos(pos_from_x, pos_from_y, pos_to_x, pos_to_y)))

                    # set_pos next
                    pieces_pos[i]['x'] = row['move']['to']['x']
                    pieces_pos[i]['y'] = row['move']['to']['y']

                    # nari
                    if row['move'].get('promote') and row['move']['piece'] == piece['name']:
                        pieces_pos[i]['name'] = switch_promote_name(piece['name'], 1)
                        print("%s) nari %s to %s" % (i, row['move']['piece'], piece['name']))

                else:
                    # set_pos
                    text_clips.append(text_clip.set_pos((pos_from_x, pos_from_y)))

                    # tori
                    if row['move'].get('capture') and row['move']['to']['x'] == piece['x'] and row['move']['to']['y'] == piece['y']:
                        print("%s) tori %s %s %s" % (i, pieces_pos[i]['name'], row['move']['to']['x'], row['move']['to']['y']))
                        # switch name
                        init_name = switch_promote_name(pieces_pos[i]['name'], 0)
                        color = 1 if pieces_pos[i]['color'] == 0 else 0
                        print("switch name and color: %s %s" % (init_name, color))

                        # add hand piece
                        add_hand_piece(hand_pieces, init_name, color)

                        # tori
                        del pieces_pos[i]
                        """
                        """

            move_clips.append(CompositeVideoClip(text_clips, size=screensize).set_duration(one_move_duration))
            count+=1

    print("pieces_pos len: %s" % len(pieces_pos))
    print(hand_pieces)

    return [concatenate_videoclips(move_clips), count]


# init pieces position
pieces_pos = set_init_pos()

# load kifu
f = open('kifu/yagura_001.jkf', 'r')
#f = open('kifu/ryuou3.jkf', 'r')
#f = open('kifu/ryuou201409020101.jkf', 'r')

json_obj = json.load(f)
moves = json_obj['moves']

# make pieces move clip
all_move_clips, count = make_clips()

# write movie file
tdatetime = datetime.datetime.today()
suffix = tdatetime.strftime('%Y%m%d_%H%M%S')
shogiban = ImageClip("img/shogiban.png").set_duration(one_move_duration*count)
video = CompositeVideoClip( [shogiban, all_move_clips],size=screensize)
video.write_videofile("./video/kifu_movie_%s.mp4" % (suffix),fps=24,codec='mpeg4')
"""
"""
