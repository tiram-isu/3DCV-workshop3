import bpy
import os

output_dir = bpy.path.abspath("//renders")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get all cameras and renderable objects
cameras = [obj for obj in bpy.data.objects if obj.type == 'CAMERA']
objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']

original_visibility = {obj.name: obj.hide_render for obj in bpy.data.objects}

for cam in cameras:
    bpy.context.scene.camera = cam  # Set active camera

    for obj in objects:
        # Hide all objects except the current one
        for o in bpy.data.objects:
            o.hide_render = True
        obj.hide_render = False  # Show only the current object

        # Set the output filepath
        filename = f"{obj.name}/{cam.name}.png"
        filepath = os.path.join(output_dir, filename)
        bpy.context.scene.render.filepath = filepath

        # Render the image
        bpy.ops.render.render(write_still=True)
        print(f"Rendered and saved: {filepath}")

# Restore original visibility
for obj_name, visibility in original_visibility.items():
    bpy.data.objects[obj_name].hide_render = visibility

print("Rendering complete.")
