#!/usr/bin/env python

from gimpfu import *

def create_button_l(img, layer) :
    #img = gimp.image_list()[0]

    drw = pdb.gimp_image_active_drawable(img)

    prev_layer = img.active_layer
    bounds = pdb.gimp_selection_bounds(img)
    width = bounds[3] - bounds[1]
    height = bounds[4] - bounds[2]
    pdb.gimp_message(width)
    pdb.gimp_message(height)
    outimg = pdb.gimp_image_new(width, height, RGB)
    layer = pdb.gimp_layer_new(outimg, width, height, RGB_IMAGE, "Back", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(outimg, layer, None, 0)

    pdb.gimp_edit_copy(img.layers[0])
    fsel = pdb.gimp_edit_paste(layer, False)
    pdb.gimp_floating_sel_to_layer(fsel)
    outimg.active_layer.name = "new.up"
    pdb.gimp_edit_copy(img.layers[1])
    fsel = pdb.gimp_edit_paste(layer, False)
    pdb.gimp_floating_sel_to_layer(fsel)
    outimg.active_layer.name = "new.over"
    pdb.gimp_edit_copy(img.layers[2])
    fsel = pdb.gimp_edit_paste(layer, False)
    pdb.gimp_floating_sel_to_layer(fsel)
    outimg.active_layer.name = "new.down"
    outimg.remove_layer(outimg.layers[3])

    img.active_layer = prev_layer

    pdb.gimp_display_new(outimg)
    pdb.gimp_displays_flush()


register(
    "python_fu_create_button_l",
    "Create button",
    "Create button from pile of layer",
    "DR",
    "MIT License",
    "2018",
    "<Image>/Test/Create button",
    "*",
    [],
    [],
    create_button_l)

main()
