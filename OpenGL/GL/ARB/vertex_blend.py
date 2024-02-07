'''OpenGL extension ARB.vertex_blend

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.vertex_blend to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides the ability to replace the single
	modelview transformation with a set of n vertex units. (Where
	n is constrained to an implementation defined maximum.) Each
	unit has its own modelview transform matrix. For each unit,
	there is a current weight associated with the vertex. When
	this extension is enabled the vertices are transformed by
	the modelview matrices of all of the enabled units. Afterward,
	these results are scaled by the weights for the respective
	units and then summed to create the eye-space vertex. A
	similar procedure is followed for the normals, except they
	are transformed by the inverse transpose of the modelview
	matrices.
	
	This extension is an orthoganalized version of functionality
	already provided by other 3D graphics API's.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/vertex_blend.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.vertex_blend import *
from OpenGL.raw.GL.ARB.vertex_blend import _EXTENSION_NAME

def glInitVertexBlendARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glWeightbvARB.weights size not checked against size
glWeightbvARB=wrapper.wrapper(glWeightbvARB).setInputArraySize(
    'weights', None
)
# INPUT glWeightsvARB.weights size not checked against size
glWeightsvARB=wrapper.wrapper(glWeightsvARB).setInputArraySize(
    'weights', None
)
# INPUT glWeightivARB.weights size not checked against size
glWeightivARB=wrapper.wrapper(glWeightivARB).setInputArraySize(
    'weights', None
)
# INPUT glWeightfvARB.weights size not checked against size
glWeightfvARB=wrapper.wrapper(glWeightfvARB).setInputArraySize(
    'weights', None
)
# INPUT glWeightdvARB.weights size not checked against size
glWeightdvARB=wrapper.wrapper(glWeightdvARB).setInputArraySize(
    'weights', None
)
# INPUT glWeightubvARB.weights size not checked against size
glWeightubvARB=wrapper.wrapper(glWeightubvARB).setInputArraySize(
    'weights', None
)
# INPUT glWeightusvARB.weights size not checked against size
glWeightusvARB=wrapper.wrapper(glWeightusvARB).setInputArraySize(
    'weights', None
)
# INPUT glWeightuivARB.weights size not checked against size
glWeightuivARB=wrapper.wrapper(glWeightuivARB).setInputArraySize(
    'weights', None
)
# INPUT glWeightPointerARB.pointer size not checked against 'type,stride'
glWeightPointerARB=wrapper.wrapper(glWeightPointerARB).setInputArraySize(
    'pointer', None
)
### END AUTOGENERATED SECTION