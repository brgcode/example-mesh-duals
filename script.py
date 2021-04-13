from compas.datastructures import Mesh
from compas.geometry import Translation, Scale, Point
from compas_view2.app import App

tetra = Mesh.from_polyhedron(4)
hexa = Mesh.from_polyhedron(6)
octa = Mesh.from_polyhedron(8)
dodeca = Mesh.from_polyhedron(12)
icosa = Mesh.from_polyhedron(20)

# ==============================================================================
# Scale and Translate
# ==============================================================================

o = Point(0, 0, 0)

T = Translation.from_vector([2.5, 0, 0])

p = Point(* tetra.vertex_coordinates(tetra.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

tetra.transform(S)

p = Point(* hexa.vertex_coordinates(hexa.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

hexa.transform(T * S)

p = Point(* octa.vertex_coordinates(octa.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

octa.transform(T * T * S)

p = Point(* dodeca.vertex_coordinates(dodeca.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

dodeca.transform(T * T * T * S)

p = Point(* icosa.vertex_coordinates(icosa.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

icosa.transform(T * T * T * T * S)

# ==============================================================================
# Viz
# ==============================================================================

viewer = App()

primal = {
    'show_faces': False,
    'show_edges': True,
    'show_vertices': False,
    'linecolor': (0, 0, 0),
    'linewidth': 2,
}

dual = {
    'show_faces': True,
    'show_edges': True,
    'show_vertices': True,
    'facecolor': (0, 0, 1),
    'linecolor': (0, 1, 1),
    'linewidth': 1,
    'pointcolor': (1, 0, 0),
    'pointsize': 20
}

viewer.add(tetra, **primal)
viewer.add(tetra.dual(), **dual)

viewer.add(hexa, **primal)
viewer.add(hexa.dual(), **dual)

viewer.add(octa, **primal)
viewer.add(octa.dual(), **dual)

viewer.add(dodeca, **primal)
viewer.add(dodeca.dual(), **dual)

viewer.add(icosa, **primal)
viewer.add(icosa.dual(), **dual)

viewer.run()