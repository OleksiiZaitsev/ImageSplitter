import re 
import os




#Oculus_Cubemap_Generator_Left_Hand
#OpenGL_Stereoscopic_Cube_Map
#Spherical_Stereoscopic
#Cube_Map_Unity
#Cube_Map
#OpenGL_CubeW
#Unity_Cube_Stereoscopic

def get_max_number_name(path,map_type) -> "return max number in name from dirs or files by path":
    dirs_names = os.listdir(path)
    list_of_numbers = []
    clear_list_names = []

    for i,n in enumerate(dirs_names):
        
        if os.path.isdir(os.path.join(path, n)) and re.findall("{} -[0-9]*".format(map_type), n):
            clear_list_names.append(n)
            
            


    
    for i in clear_list_names:
        number = re.findall('.*([-_][0-9]+).*', i)
        if number:
            list_of_numbers.append(*number)


    try:
        max_number = max([int(re.sub('[-_]', '', i)) for i in list_of_numbers])
    except:
        max_number = 0


    return str(max_number + 1)


print(get_max_number_name(r"R:\GraphicsGroup\UXDesignPart\Projects\Proposal_2017\3dsMax_Underwater\Render\cube", "Unity_Cube_Stereoscopic"))