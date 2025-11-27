
import random, webbrowser

from PIL import Image

import maya.cmds as cmds

SAVE_PATH = 'D:/Desktop/test.png'

def lerpFactor(a, b, value):
    return (value - a) / (b - a)

def generateTexture(data, width, height):

    img = Image.new('RGB', (width, height))
    img.putdata(data)

    return img

def run():

    vertex_animation = []

    selected_mesh = cmds.ls(sl=1, typ='transform')[0]
    selected_mesh_vertices = cmds.ls(selected_mesh + ".vtx[*]", fl=1)

    start_frame = int(cmds.playbackOptions(q=1, ast=1))
    end_frame = int(cmds.playbackOptions(q=1, aet=1))
    for frame in range(start_frame, end_frame + 1):

        frame_vertex_positions = []

        for vertexId, vertex in enumerate(selected_mesh_vertices):
            vertex_position = cmds.xform(vertex, q=1, t=1)
            frame_vertex_positions.extend(vertex_position)

        vertex_animation.extend(frame_vertex_positions)

    min_transform = min(vertex_animation)
    max_transform = max(vertex_animation)

    vertex_animation_normalized = [int(lerpFactor(min_transform, max_transform, transform) * 255) for transform in vertex_animation]
    
    vertex_animation_bundled = []
    for i in range(0, len(vertex_animation_normalized), 3):
        vertex_animation_bundled.append(tuple(vertex_animation_normalized[i:i+3]))

    return generateTexture(vertex_animation_bundled, len(selected_mesh_vertices), end_frame - start_frame + 1)

run().save(SAVE_PATH)
webbrowser.open(SAVE_PATH)
