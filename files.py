import csv   # nos permite trabajad con archivos de tipo cvs
import json  # nos permite trabajar con archivos de tipo json
import os    # nos ayuda que exista un mejor flujo al trabajar en el computador 

FOLDER_DATA =   "data"  # carpeta doonde se va a almacenar todos los datos (persistentes)
FILES_JSON = os.path.join(FOLDER_DATA,"data.json") 
FILES_CSV = os.path.join(FOLDER_DATA, "data.csv")

#Esta funcion permite crear una carperta para almacenar los datos si no esta no existe de manera automatica
def make_folder_if_not_exist():
    if not os.path.exists(FOLDER_DATA):

        os.makedirs(FOLDER_DATA)    

#Funcion que permite leer los datos y cargarlos como JSON
def read_registers_json():
    if not os.path.exists(FILES_JSON):
        return[]
    with open(FILES_JSON, "r", encoding="utf-8") as file:
        return json.load(file)
    

#Funcion que permite guardar los datos y ecribilos en JSON y retornar en formato de diccionario
def save_registers_json(registers):
    make_folder_if_not_exist()
    with open(FILES_JSON, "w", encoding=" utf-8") as file:
        json.dump(registers,file, indent=4, ensure_ascii= False)


#Funcion que perimite hacer un nuevo regisrto
def maker_register(register):
    registers = read_registers_json()
    registers.append(register)
    save_registers_json(registers)


#Permite acualizar los datos
def update_register(id_vaule, id_camp, new_register):
    registers = read_registers_json()
    for register in registers:
        if register.get(id_camp) == id_vaule:
            register.update(new_register)
            save_registers_json(registers)
            return True
    return False


#permite borrar los datos
def delete_register_json(id_vaule, id_camp):
    registers = read_registers_json()
    new_registers = []
    delete = False
    for register in registers:
        if register.get(id_camp) == id_vaule:
            delete = True
        else:
            new_registers.append(register)
    if delete:
        save_registers_json(new_registers)
        return True
    return False

#permite buscar el registro por numero de ID
def look_for__id(id_vaule, id_camp):
    registers = read_registers_json()

    for register in registers:
        if str(register.get(id_camp)) == str(id_vaule):
            return register
    return None


#perite exportar los datos guardados en JSON a CSV
def export_for_csv():
    registers = read_registers_json()
    if not registers:
        print("It has not register for export")
        return
    with open (FILES_CSV, "w", newline="", encoding="utf-8") as file_cvs:
        writer_csv = csv.DictWriter(file_cvs, fieldnames=registers[0].keys())
        writer_csv.writeheader()
        writer_csv.writerows(registers)
    print(f"Registers was export for {FILES_CSV}")
    
