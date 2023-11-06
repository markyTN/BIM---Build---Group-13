from pathlib import Path
import ifcopenshell

#The script has been developed with help from chatGPT.
# Function to modify material names based on a mapping
def modify_materials(model, material_mapping):
    # Iterate through the IfcBeam instances
    ifc_beams = model.by_type("IfcBeam")
    for beam in ifc_beams:
        for association in beam.HasAssociations:
            if association.is_a("IfcRelAssociatesMaterial"):
                material_association = association.RelatingMaterial
                if material_association.is_a("IfcMaterial"):
                    material_name = material_association.Name
                    # Check if the material name is in the mapping
                    if material_name in material_mapping:
                        # Update the material name
                        material_association.Name = material_mapping[material_name]

# Load the model
modelname = "LLYN - STRU" #Change to the appropriate model name

try:
    dir_path = Path(__file__).parent
    model_url = Path.joinpath(dir_path, 'model', modelname).with_suffix('.ifc')
    model = ifcopenshell.open(model_url)
except OSError:
    try:
        import bpy
        model_url = Path.joinpath(Path(bpy.context.space_data.text.filepath).parent, 'model', modelname).with_suffix('.ifc')
        model = ifcopenshell.open(model_url)
    except OSError:
        print(f"ERROR: please check your model folder: {model_url} does not exist")

# Define a mapping of materials to update
material_mapping = {
    "4. (SB) Stålbjælke": "Rustfrit Stål", #"previous material : New material"
    "@_SB_Stål": "Beton"
}

# Modify the materials
modify_materials(model, material_mapping)

# Save the modified IFC model to a new file
modified_model_path = 'C:/Users/tina/OneDrive/DTU/K1/BIM/A3/A3 - Script + model/model/modified_model.ifc' #Change to the appropriate path
model.write(modified_model_path) #To save a new file, change the name - to overwrite, keep the same name file

print("Material modification complete. Modified model saved at:", modified_model_path)
