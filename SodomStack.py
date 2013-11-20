import ase
from ase.utils.geometry import cut, stack
from ase import io
from ase import atoms



# Read in the configurations
substrate = ase.io.read('POSCAR.SnO.vasp',format='vasp')
epilayer  = ase.io.read('POSCAR.NiO.vasp',format='vasp')

# Rotate the epilayer
angle_of_rotation = 0.5      #  The increment of rotation
centre_of_mass = epilayer.get_center_of_mass()
epilayer.rotate([0,0,1], angle_of_rotation, center=centre_of_mass, rotate_cell=True)

# Translate the epilayer
translation_vector = [0.2, 0.0, 0.0]    # The amount to translate by
epilayer.translate(translation_vector)


# Generate the interface
NewSurface = stack(substrate, epilayer, axis = 2, fix = 0, maxstrain=None)

# Output
ase.io.write('Stack.cif', NewSurface, format='cif')
