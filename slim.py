# SCons profile for slim Godot export templates: pass as `profile=slim.py`.
#
# Built for pure-2D games drawn with Controls (EVEN STEVEN first). The renderer
# is left exactly as stock: RenderingDevice (Vulkan, Metal) and OpenGL stay,
# and so do AccessKit and the advanced text server.
#
# Every switch here removes something the stock template has. A class a game
# needs but this build lacks fails only at runtime, when the scene or script
# using it loads — so after changing this file, play the game through on
# every platform before shipping it.

production = "yes"
optimize = "size"
lto = "full"
debug_symbols = "no"

# Whole subsystems a 2D Control game never touches.
disable_3d = "yes"
disable_physics_3d = "yes"
disable_navigation_3d = "yes"
disable_xr = "yes"
disable_physics_2d = "yes"
disable_navigation_2d = "yes"

# Modules: none unless listed. EVEN STEVEN needs GDScript, TTF fonts through
# the advanced text server, MP3 audio, and lossless textures (PNG is core,
# WebP is a module). SVG is kept for the text server's colour glyphs and the
# runtime icon. Keep advanced GUI: ConfirmationDialog lives there.
modules_enabled_by_default = "no"
module_gdscript_enabled = "yes"
module_freetype_enabled = "yes"
module_text_server_adv_enabled = "yes"
module_svg_enabled = "yes"
module_webp_enabled = "yes"
module_mp3_enabled = "yes"

# The RenderingDevice renderers (Vulkan, Metal, D3D12) compile their shaders
# at runtime through glslang. Without it a fresh install renders nothing —
# and a machine that already has the game's shader cache from a stock build
# hides that, so test with an empty user data directory.
module_glslang_enabled = "yes"
