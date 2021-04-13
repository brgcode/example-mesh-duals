from compas.datastructures import Mesh
from compas.geometry import Translation, Scale, Point

tetra = Mesh.from_polyhedron(4)
hexa = Mesh.from_polyhedron(6)
octa = Mesh.from_polyhedron(8)
dodeca = Mesh.from_polyhedron(12)
icosa = Mesh.from_polyhedron(20)

o = Point(0, 0, 0)

T = Translation.from_vector([2.5, 0, 0])

p = Point(* tetra.vertex_coordinates(tetra.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

tetra.transform(S)
tetra.dual()

p = Point(* hexa.vertex_coordinates(hexa.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

hexa.transform(T * S)
hexa.dual()

p = Point(* octa.vertex_coordinates(octa.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

octa.transform(T * T * S)
octa.dual()

p = Point(* dodeca.vertex_coordinates(dodeca.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

dodeca.transform(T * T * T * S)
dodeca.dual()

p = Point(* icosa.vertex_coordinates(icosa.get_any_vertex()))
s = 1 / (p - o).length
S = Scale.from_factors([s, s, s])

icosa.transform(T * T * T * T * S)
icosa.dual()
