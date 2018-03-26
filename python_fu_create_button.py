#!/usr/bin/env python

import os
from gimpfu import *

current_path = os.getcwd()


def create_button(img, layer, name, dist, path_name):
    prev_layer = img.active_layer
    non_empty, x1, y1, x2, y2 = pdb.gimp_selection_bounds(img)
    if non_empty:
        width = x2 - x1
        height = y2 - y1
        out_img = pdb.gimp_image_new(width, height, RGB)
        layer = pdb.gimp_layer_new(out_img, width, height, RGBA_IMAGE, "Background", 100,
                                   NORMAL_MODE)
        pdb.gimp_image_insert_layer(out_img, layer, None, 0)
        suffix = [".up", ".down", ".over"]
        index = 0
        last = 3 if len(img.layers) > 3 else len(img.layers)
        while index < last:
            pdb.gimp_edit_copy(img.layers[index])
            pdb.gimp_floating_sel_to_layer(pdb.gimp_edit_paste(layer, False))
            out_img.active_layer.name = name + suffix[index]
            if dist == 1:
                file_name = name + suffix[index] + ".png"
                full_path = os.path.join(path_name, file_name)
                pdb.file_png_save_defaults(out_img, out_img.active_layer, full_path,
                                           file_name)
            index = index + 1
        out_img.remove_layer(out_img.layers[len(out_img.layers) - 1])
        img.active_layer = prev_layer
        if dist == 0:
            pdb.gimp_display_new(out_img)
            pdb.gimp_displays_flush()
    else:
        pdb.gimp_message("Please select area for button")


register(
    "python_fu_create_button",
    "Create button from pile of layers",
    """Create button from pile of layers  below selected area
     with name: button.up, button.down, button.over """,
    "DR",
    "MIT License",
    "2018",
    "<Image>/Script/Create button...",
    "*",
    [
        (PF_STRING, "name", "Common name of layers", "button"),
        (PF_RADIO, "dist", "Save to:", 0, (("layers", 0), ("files", 1))),
        (PF_DIRNAME, "path_name", "Output directory", current_path)
    ],
    [],
    create_button)

main()
