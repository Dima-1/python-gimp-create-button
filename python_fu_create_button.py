#!/usr/bin/env python

from gimpfu import *


def create_button(img, layer, name):
    prev_layer = img.active_layer
    bounds = pdb.gimp_selection_bounds(img)
    width = bounds.x2 - bounds.x1
    height = bounds[4] - bounds[2]
    outimg = pdb.gimp_image_new(width, height, RGB)
    layer = pdb.gimp_layer_new(outimg, width, height, RGBA_IMAGE, "Background", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(outimg, layer, None, 0)

    pdb.gimp_edit_copy(img.layers[0])
    fsel = pdb.gimp_edit_paste(layer, False)
    pdb.gimp_floating_sel_to_layer(fsel)
    outimg.active_layer.name = name + ".up"
    pdb.gimp_edit_copy(img.layers[1])
    fsel = pdb.gimp_edit_paste(layer, False)
    pdb.gimp_floating_sel_to_layer(fsel)
    outimg.active_layer.name = name + ".over"
    pdb.gimp_edit_copy(img.layers[2])
    fsel = pdb.gimp_edit_paste(layer, False)
    pdb.gimp_floating_sel_to_layer(fsel)
    outimg.active_layer.name = name + ".down"
    outimg.remove_layer(outimg.layers[3])

    img.active_layer = prev_layer

    pdb.gimp_display_new(outimg)
    pdb.gimp_displays_flush()


register(
    "python_fu_create_button",
    "Create button",
    "Create button from pile of layers",
    "DR",
    "MIT License",
    "2018",
    "<Image>/Script/Create button...",
    "*",
    [(PF_STRING, "name", "Layers name", "button")],
    [],
    create_button)

main()
