import sys

if __name__ == '__main__':
    if len(sys.argv) > 3:
        print("Error:")
        print("\tPer utilitzar la implementació has de posar només 1 o cap .txt desprès de cridar-ho.")
        print(f"\tPer exemple:\n\t\tpy {sys.argv[0]} \"OPT22-23_Datos práctica 2\"")
        print(f"\tPer exemple:\n\t\tpy {sys.argv[0]} \"OPT22-23_Datos práctica 2\" [qualsevol cosa]")
    else:
        path_flow = []
        path_inters = {}
        inters_neight = {}
        if len(sys.argv) == 1:
            file = "OPT22-23_Datos práctica 2"
        else:
            file = sys.argv[1]
        with open(f'./Data/{file}.txt', 'r', encoding = 'UTF-8') as f:
            f.readline()
            inters = f.readline().split("\t")
            inters = list(filter(('').__ne__, inters))
            inters.remove("\n")

            jump = f.readline()
            while jump == "\n":
                jump = f.readline()

            paths = f.readline().split("\t")
            paths[len(paths) - 1] = paths[len(paths) - 1].split("\n")[0]
            paths = list(filter(('').__ne__, paths))

            jump = f.readline()
            while jump == "\n":
                jump = f.readline()

            fixed = f.readline().split(" ")
            fixed[len(fixed) - 1] = fixed[len(fixed) - 1].split("\n")[0]

            jump = f.readline()
            while jump == "\n":
                jump = f.readline()

            prohibed = f.readline().split(" ")
            prohibed[len(prohibed) - 1] = prohibed[len(prohibed) - 1].split("\n")[0]

            jump = f.readline()
            while jump == "\n":
                jump = f.readline()

            #El fluxe ha d'estar ordenat de la mateixa manera que els paths
            #  en el fitxer de data
            flux = f.readline().split(" ")
            while flux[0] != "\n":
                path_flow += [eval(flux[len(flux) - 1].split("\n")[0])]
                flux = f.readline().split(" ")

            jump = f.readline()
            while jump == "\n":
                jump = f.readline()

            pathline = f.readline().split(" ")
            while pathline[0] != "\n":
                if not (pathline[0] in path_inters):
                    path_inters[pathline[0]] = [pathline[1].split("\n")[0]]
                else:
                    path_inters[pathline[0]] += [pathline[1].split("\n")[0]]
                pathline = f.readline().split(" ")

            jump = f.readline()
            while jump == "\n":
                jump = f.readline()
            
            neightline = f.readline().split(" ")
            while neightline[0] != "\n":
                if not (neightline[0] in inters_neight):
                    inters_neight[neightline[0]] = [neightline[1].split("\n")[0]]
                else:
                    inters_neight[neightline[0]] += [neightline[1].split("\n")[0]]
                neightline = f.readline().split(" ")

        inters_str = "set INTERS := "
        for x in inters:
            inters_str += f"\"{x}\" "
        inters_str += ";"
        
        paths_str = "set PATHS := "
        for x in paths:
            paths_str += f"\"{x}\" "
        paths_str += ";"

        fixed_str = "set FIXED := "
        for x in fixed:
            fixed_str += f"\"{x}\" "
        fixed_str += ";"

        prohibed_str = "set PROHIBITED := "
        for x in prohibed:
            prohibed_str += f"\"{x}\" "
        prohibed_str += ";"

        path_flow

        path_flow_str = "param flows := "
        i = 0
        for x in path_flow:
            path_flow_str += f"\"{paths[i]}\" {x} "
            i += 1
        path_flow_str += ";"

        path_inters_str1 = "set PATH_INTER := "
        for x in path_inters:
            path_inters_str1 += f"(\"{x}\",*) "
            for y in path_inters[x]:
                path_inters_str1 += f"\"{y}\" "
            path_inters_str1 += "\n"
        path_inters_str1 += ";"

        param_f = "param f :=\n"
        for x in paths:
            param_f += f"[\"{x}\",*] "
            for y in inters:
                if y in path_inters[x]:
                    param_f += f"\"{y}\" 1 "
                else:
                    param_f += f"\"{y}\" 0 "
            param_f += "\n"
        param_f += ";"

        
        

        inters_neight_str1 = "set INTERS_NEIGHT := "
        for x in inters_neight:
            inters_neight_str1 += f"(\"{x}\",*) "
            for y in inters_neight[x]:
                inters_neight_str1 += f"\"{y}\" "
            inters_neight_str1 += "\n"
        inters_neight_str1 += ";"
        if len(sys.argv) < 2:
            with open(f"data/sensor.dat", 'w') as f:
                towrite = ["data;","\n\n",inters_str,"\n\n", paths_str,"\n\n", fixed_str,"\n\n",
                            prohibed_str,"\n\n",
                        path_flow_str,"\n\n", 
                        param_f,"\n\n",
                        ]
                f.writelines(towrite)
        
        else:
            with open(f"data/sensor2.dat", 'w') as f:
                towrite = ["data;","\n\n",inters_str,"\n\n", paths_str,"\n\n", fixed_str,"\n\n",
                        prohibed_str,"\n\n",path_flow_str,"\n\n",path_inters_str1,"\n\n",
                        inters_neight_str1,"\n\n",]
                f.writelines(towrite)

        print("Finished")