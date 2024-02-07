'''OpenGL extension EXT.YUV_target

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.YUV_target to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds support for three new YUV related items: first
	rendering to YUV images, second sampling from YUV images while keeping the
	data in YUV space, third it defines a new built in function that does
	conversion from RGB to YUV with controls to choose ITU-R BT.601-7,
	ITU-R BT.601-7 Full range (JFIF images), or ITU-R BT.709-5 standard.
	
	This new functionality is layered on top of the OES_EGL_image_external
	extension.
	
	To perform the YUV rendering capability in this extension an application
	will attach a texture to the framebuffer object as the color attachment.
	If the texture has a target type of TEXTURE_EXTERNAL_OES with YUV color
	format then the GL driver can use this framebuffer object as the render
	target, TEXTURE_EXTERNAL_OES target with RGB color format are not allowed
	with this extension.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/YUV_target.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.YUV_target import *
from OpenGL.raw.GLES2.EXT.YUV_target import _EXTENSION_NAME

def glInitYuvTargetEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION