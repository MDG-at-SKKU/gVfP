from ase import io
from ase.data import atomic_numbers, covalent_radii

def genVESTAfromPOSCAR(filename,savename,color_data):
    x = io.read(filename)
    
    a = open(savename,'w')
    a.write('#VESTA_FORMAT_VERSION 3.5.4\n\n\nCRYSTAL\n\nTITLE\n VESTA from POSCAR\n\nCELLP\n ')
    temp = x.cell.cellpar()
    for i in range(len(temp)):
        a.write("{:.6f}".format(temp[i]) + '  ')
    a.write('\n  0.000000   0.000000   0.000000   0.000000   0.000000   0.000000\nSTRUC\n')
    
    
    for i in range(len(x)):
        if i == 0:
            counter = 1
        else:
            if x.get_chemical_symbols()[i] == x.get_chemical_symbols()[i-1]:
                counter += 1
            else:
                counter = 1
                
        temp1 = "{: >3}".format(i+1)
        temp2 = "{: >2}".format(x.get_chemical_symbols()[i])
        temp3 = "{: >11}".format(str(x.get_chemical_symbols()[i]) + str(counter))
        temp4 = '  1.0000   '
        temp5 = '   '.join(f"{val:.6f}" for val in x[i].scaled_position) + '    1a       1 ' + '\n'
        temp = temp1 + ' ' + temp2 + temp3 + temp4 + temp5
        a.write(temp)
        a.write('                            0.000000   0.000000   0.000000  0.00\n')
    a.write('  0 0 0 0 0 0 0\nSITET\n')
   
    for i in range(len(x)):
        temp1 = "{: >3}".format(i+1)
        temp2 = "{: >11}".format(str(x.get_chemical_symbols()[i]) + str(counter))
        temp3 = "{: >6}".format(covalent_radii[atomic_numbers[x[i].symbol]])
        temp4 = str(color_data[i][0]).rjust(3, ' ') +  ' ' + str(color_data[i][1]).rjust(3, ' ') + ' ' + str(color_data[i][2]).rjust(3, ' ')
        a.write(temp1 + temp2 + temp3 + ' ' + temp4 + ' ' + temp4 + ' 204  0' + '\n')
    a.write('  0 0 0 0 0 0\n')
    a.close()
    