This project is a simple visualization of Hartree-Fock method.
It is primarily a single web app written in python.
It has a selector dropdown menu to select the molecule and another dropdown menu to select the basis set. These options use common libraries for molecules and basis sets, such as PySCF and Basis Set Exchange.
for a 3D visualization of the molecular orbitals, it uses Plotly, which is a powerful library for creating interactive visualizations in Python. The app allows users to visualize the molecular orbitals in 3D, providing insights into the electronic structure of the selected molecule. Overall, this project serves as an educational tool for understanding the Hartree-Fock method and its applications in computational chemistry.
After selecting the molecule the app will update the molecule 3D shape immediately in the frame. 
After selecting the basis set the app will update the Coeffcients matrix and the orbital energies in another frame.
There will be a button that will start the HF calculation. It will update the Coefficients matrix and the slater determinant and the HF wavefunction in another frame.
After each SCF loop converges, the app will update overal energy and the forces on the atoms and when it moves on to the next SCF loop, it will update the 3D shape of the molecule as well.
eventuall there will always be a counter for the number of SCF operations it took to converge for every loop and also another counter for the total number of SCF loops used to reach the ground state energy. 
