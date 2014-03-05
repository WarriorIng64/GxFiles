# This file is part of GxFiles.
# Copyright (C) 2014 Christopher Kyle Horton <christhehorton@gmail.com>

# GxFiles is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# GxFiles is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GxFiles. If not, see <http://www.gnu.org/licenses/>.


# Window and UI code------------------------------------------------------------

window = self.CreateWindow(48, 0, 600, 400, 'GxFiles')
window.SetIcon("apps/default/GxFiles/")

vbox1 = VBox(window.top_level_container, window, [])
window.AddWidget(vbox1)

hbox_top_buttons = HBox(vbox1, window, [])
hbox_top_buttons.RequestHeight(32)
hbox_main_area = HBox(vbox1, window, [])
window.AddWidget(hbox_top_buttons, vbox1)
window.AddWidget(hbox_main_area, vbox1)

button_go_up = Button(hbox_top_buttons, window, "Go Up", "")
button_go_up.RequestWidth(64)
button_add_bookmark = Button(hbox_top_buttons, window, "Add Bookmark", "")
button_add_bookmark.RequestWidth(128)
window.AddWidget(button_go_up, hbox_top_buttons)
window.AddWidget(button_add_bookmark, hbox_top_buttons)

vbox_bookmarks = VBox(hbox_main_area, window, [])
vbox_bookmarks.RequestWidth(100)
window.AddWidget(vbox_bookmarks, hbox_main_area)
bookmarks_label = Label(vbox_bookmarks, window, "Bookmarks")
bookmarks_label.RequestHeight(32)
window.AddWidget(bookmarks_label, vbox_bookmarks)

# Temporary until we have dynamically-created bookmarks
button_bookmark1 = Button(vbox_bookmarks, window, "Bookmark 1", "")
button_bookmark1.RequestHeight(32)
button_bookmark2 = Button(vbox_bookmarks, window, "Bookmark 2", "")
button_bookmark2.RequestHeight(32)
button_bookmark3 = Button(vbox_bookmarks, window, "Bookmark 3", "")
button_bookmark3.RequestHeight(32)
window.AddWidget(button_bookmark1, vbox_bookmarks)
window.AddWidget(button_bookmark2, vbox_bookmarks)
window.AddWidget(button_bookmark3, vbox_bookmarks)

# Temporary until we have an actual content area
label_content_area = Label(hbox_main_area, window, "(Coming soon!)")
window.AddWidget(label_content_area, hbox_main_area)
