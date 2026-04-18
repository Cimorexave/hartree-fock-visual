import numpy as np
from pyscf import gto, scf

# This list will store our "frames" for the visualization
scf_history = []

def callback(envs):
    """
    This function runs at the end of every SCF iteration.
    'envs' contains the current state of the calculation.
    """
    # Grab the current iteration data
    iteration_data = {
        'iteration': len(scf_history) + 1,
        'total_energy': envs['last_e'],
        'fock_matrix': envs['f'].copy(),      # The F matrix you want to visualize
        'density_matrix': envs['mo_occ'],    # Useful for seeing electron distribution
        'mo_coeffs': envs['mo_coeff'].copy() # The C matrix (coefficients)
    }
    scf_history.append(iteration_data)
    print(f"Iteration {iteration_data['iteration']}: E = {iteration_data['total_energy']:.8f}")

# 1. Setup the molecule from SMILES (or manual coords)
mol = gto.M(atom='O 0 0 0; H 0 1 0; H 0 0 1', basis='sto-3g')

# 2. Setup the SCF object
mf = scf.RHF(mol)

# 3. Attach the callback
mf.callback = callback

# 4. Run!
print("Starting SCF Loop...")
mf.kernel()

print(f"\nCaptured {len(scf_history)} iterations for the visualizer.")