from pathlib import Path
import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.classification
import ifcopenshell.util.unit

modelname = "LLYN - STRU"

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
        print(f"ERROR: please check your model folder : {model_url} does not exist")

# Your script goes here
#The script has been developed with help from chatGPT. The probing question used were "What data are available and can be extracted from the IFC model", "How do we extract data from Qto_SlabBaseQuantities" and "how to combine script into one" and more. 

#BEAM
#The following script extract information from IfcBeam, which includes Name, ID, type, length, area, volume, it's location and the material associated to it. 
#These information are supposed to help the project manager identify and calculate the cost of the construction part of the project. 


beam_in_model = len(model.by_type("IfcBeam")) #Calculating the number of beams in the model
print(f"\nThere are {beam_in_model} beams in the model") 

# Define unit for length, area, and volume
unit_mappings = {
    "Length": "mm",
    "CrossSectionArea": "m2",
    "NetVolume": "m3"
}


# Define a function to get the story or level of an element
def get_story(element):
    for rel in element.ContainedInStructure:
        if rel.is_a("IfcRelContainedInSpatialStructure"):
            container = rel.RelatingStructure
            if container.is_a("IfcBuildingStorey"):
                return container.Name
    return "N/A"

# Define a list to store data for beams
beam_data = []
all_materials = []

# Define the relevant Quantity Set for Beams by its name
target_quantity_set_name = "Qto_BeamBaseQuantities"

# Get all instances of IfcBeam in the IFC file
ifc_beams = model.by_type("IfcBeam")

# Iterate through the IfcBeam instances
for beam in ifc_beams:
    # Extract and store beam properties (Type, ID, Name)
    beam_properties = {
        "Type": beam.is_a(),
        "GlobalId": beam.GlobalId,
        "Name": beam.Name,
        "Story/Level": get_story(beam)
    }

    # Check if the beam has relevant quantity information (length, area, and volume)
    for quantity_set in beam.IsDefinedBy:
        if (
            hasattr(quantity_set, "RelatingPropertyDefinition")
            and quantity_set.RelatingPropertyDefinition.is_a("IfcElementQuantity")
            and quantity_set.RelatingPropertyDefinition.Name == target_quantity_set_name
        ):
            # Iterate through the quantities within the Quantity Set
            for quant in quantity_set.RelatingPropertyDefinition.Quantities:
                # Check if the quantity corresponds to a beam property
                if quant.Name in unit_mappings:
                    # Extract and store the quantity name and value
                    quantity_name = quant.Name

                    # Get the value based on the quantity type
                    if hasattr(quant, "LengthValue"):
                        quantity_value = quant.LengthValue
                    elif hasattr(quant, "AreaValue"):
                        quantity_value = quant.AreaValue
                    elif hasattr(quant, "VolumeValue"):
                        quantity_value = quant.VolumeValue
                    else:
                        quantity_value = None

                    # Assign the unit based on the quantity type
                    unit = unit_mappings.get(quantity_name, "Unknown")

                    # Assign the data with unit information
                    beam_properties[quantity_name] = f"{quantity_value} {unit}"

    # Find the material associated with the beam
    for association in beam.HasAssociations:
        if association.is_a("IfcRelAssociatesMaterial"):
            material_association = association.RelatingMaterial
            if material_association.is_a("IfcMaterial"):
                material_name = material_association.Name
                beam_properties["Material"] = material_name
                all_materials.append(material_name)

    # Append the beam properties to the beam_data list
    beam_data.append(beam_properties)


# Print the data for beams with Type, ID, Name, Length, Area, Volume, Material, and Story/Level
for data in beam_data:
    print("Type:", data["Type"])
    print("GlobalId:", data["GlobalId"])
    print("Name:", data["Name"])
    print("Length:", data.get("Length", "N/A"))
    print("CrossSectionArea:", data.get("CrossSectionArea", "N/A"))
    print("NetVolume:", data.get("NetVolume", "N/A"))
    print("Material:", data.get("Material", "N/A"))
    print("Story/Level:", data.get("Story/Level", "N/A"))
    print("-" * 40)


#COLUMN
#The following script extract information from IfcColumn, which includes Name, ID, type, length, area, volume, it's location and the material associated to it . 
#These information are supposed to help the project manager identify and calculate the cost of the construction part of the project. 

column_in_model = len(model.by_type("IfcColumn")) #Calculating the number of columns in the model
print(f"\nThere are {column_in_model} columns in the model") 

# Define unit for length, area, and volume
unit_mappings = {
    "Length": "mm",
    "CrossSectionArea": "m2",
    "NetVolume": "m3"
}


# Define a function to get the story or level of an element
def get_story(element):
    for rel in element.ContainedInStructure:
        if rel.is_a("IfcRelContainedInSpatialStructure"):
            container = rel.RelatingStructure
            if container.is_a("IfcBuildingStorey"):
                return container.Name
    return "N/A"

# Define a list to store data for columns
column_data = []
all_materials = []

# Define the relevant Quantity Set for columns by its name
target_quantity_set_name = "Qto_ColumnBaseQuantities"

# Get all instances of IfcColumn in the IFC file
ifc_columns = model.by_type("IfcColumn")

# Iterate through the IfcColumn instances
for column in ifc_columns:
    # Extract and store column properties (Type, ID, Name)
    column_properties = {
        "Type": column.is_a(),
        "GlobalId": column.GlobalId,
        "Name": column.Name,
        "Story/Level": get_story(column)
    }

    # Check if the column has relevant quantity information (length, area, and volume)
    for quantity_set in column.IsDefinedBy:
        if (
            hasattr(quantity_set, "RelatingPropertyDefinition")
            and quantity_set.RelatingPropertyDefinition.is_a("IfcElementQuantity")
            and quantity_set.RelatingPropertyDefinition.Name == target_quantity_set_name
        ):
            # Iterate through the quantities within the Quantity Set
            for quant in quantity_set.RelatingPropertyDefinition.Quantities:
                # Check if the quantity corresponds to a column property
                if quant.Name in unit_mappings:
                    # Extract and store the quantity name and value
                    quantity_name = quant.Name

                    # Get the value based on the quantity type
                    if hasattr(quant, "LengthValue"):
                        quantity_value = quant.LengthValue
                    elif hasattr(quant, "AreaValue"):
                        quantity_value = quant.AreaValue
                    elif hasattr(quant, "VolumeValue"):
                        quantity_value = quant.VolumeValue
                    else:
                        quantity_value = None

                    # Assign the unit based on the quantity type
                    unit = unit_mappings.get(quantity_name, "Unknown")

                    # Assign the data with unit information
                    column_properties[quantity_name] = f"{quantity_value} {unit}"

    # Find the material associated with the column
    for association in column.HasAssociations:
        if association.is_a("IfcRelAssociatesMaterial"):
            material_association = association.RelatingMaterial
            if material_association.is_a("IfcMaterial"):
                material_name = material_association.Name
                column_properties["Material"] = material_name
                all_materials.append(material_name)

    # Append the column properties to the column_data list
    column_data.append(column_properties)


# Print the data for columns with Type, ID, Name, Length, Area, Volume, Material, and Story/Level
for data in column_data:
    print("Type:", data["Type"])
    print("GlobalId:", data["GlobalId"])
    print("Name:", data["Name"])
    print("Length:", data.get("Length", "N/A"))
    print("CrossSectionArea:", data.get("CrossSectionArea", "N/A"))
    print("NetVolume:", data.get("NetVolume", "N/A"))
    print("Material:", data.get("Material", "N/A"))
    print("Story/Level:", data.get("Story/Level", "N/A"))
    print("-" * 40)
