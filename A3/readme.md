##### A3 - OpenBIM Change

###### Identify the IFC entities and properties you will need for your use case.

The IFC entities in focus are IfcBeam, IfcColumn, which represent some of the construction elements. In terms of IFC properties, we will be working with IfcElementQuantity and IfcMaterial, which contains information about geometrics properties and materials properties.  

###### Model Uses

This tool is designed for the project manager and the craftsmen on the construction site. Its purspose is to optimize the construction process and make project management simpler by assisting in material management, schedule coordination and cost estimation by using BIM data. 
The additional feature, which involves modifying the material in the IFC model, is supposed to simplify any modification process. This can be useful in cases such as price changes in materials or unexpected delays or unavailability of the products.
Our tool is expected to have a high level of detailing as it must be able to specify the specific material to be used in the project. To use our tool you need to know about the costs of the various materials and the exact quantities. In that way the level of detail of the output depends on the level of detail of the input. 

###### Process
General architectural concept and material choices for the building need to be accomplished before material management, schedule coordination and cost estimation can be begun.  When our use case has be done, the use cases in construction phase can begin, these includes site preparation, foundation construction, structural framing and more. 

###### Description of the process of your tool / workflow.
The process of our tool can be view on A3-BIM-UseCase.svg

The red box represents the part of the developed script, which focuses on the early stages of the use case, which is to extract information from the project’s objects and their associated properties and compile a list of details that includes Name, GlobalID, type, length, area, volume, it’s location and the material associated with the element. This is supposed to make the classification of the construction elements easier.  

The green box represents the part that we would like to implement into our use case. The developed script makes it possible to modify the already existing material in the model. This script loads the original model, modifies the materials according to user input and saves the file as new. The intention is to create a tool that makes it easy and fast to modify the IFC model with python.  

###### Describe the business value (How does it create value for your business/employer)

The tool creates value for the business as you can save time by using it to calculate costs and quantities of materials. In addition to saving time, it also makes the entire construction process more flexible as you can create an overview of the project and see the consequences and benefits (in terms of cost) of replacing different materials with something else. It is a great advantage to know these things in the early design phase.  

###### Describe the societal value (How does it make the world better)

Since you can calculate the costs for different materials you can save money by using the cheaper materials. The tool can also be further developed so that it calculates the CO2footprint of the various materials and in that way you can use it to choose the most sustainable solution.
