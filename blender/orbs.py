import numpy as np
from numpy.random import random as rnd
import bpy
import bmesh

# convenience Variables: C = bpy.context, D = bpy.data
C = bpy.context
D = bpy.data
scene = C.scene


def make_sphere(name, location, size, u_segs=32, v_segs=16):
    # Create an empty mesh and the object.
    mesh = D.meshes.new("%s Mesh" % name)
    sphere = D.objects.new(name, mesh)

    # Add the object into the scene.
    scene.objects.link(sphere)
    scene.objects.active = sphere

    # Construct the bmesh cube and assign it to the blender mesh.
    geometry = bmesh.new()
    bmesh.ops.create_uvsphere(geometry, u_segments=u_segs, v_segments=v_segs, diameter=size)
    geometry.to_mesh(mesh)
    sphere.location = location
    geometry.free()


for obj in bpy.data.objects:
    if 'g_' in obj.name:
        bpy.data.objects.remove(obj)

for i in range(10):
    make_sphere("g_sphere_%d" % i, rnd(3) * 10 - 5, 1)

for sphere in [obj for obj in bpy.data.objects if 'g_' in obj.name]:


