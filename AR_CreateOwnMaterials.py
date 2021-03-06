"""
AR_CreateOwnMaterials

Author: Arttu Rautio (aturtur)
Website: http://aturtur.com/
Name-US: AR_CreateOwnMaterials
Description-US: Creates own materials for selected objects from existing materials
Written for Maxon Cinema 4D R20.057
"""
# Libraries
import c4d

# Functions
def main():
    doc = c4d.documents.GetActiveDocument() # Get active Cinema 4D document
    doc.StartUndo() # Start recording undos
    try: # Try to execute following script
        selection = doc.GetSelection() # Get active selection
        for x in reversed(selection): # Loop through reversed selection
            if isinstance(x, c4d.BaseObject): # If item is instance of Base Object
                tags = x.GetTags() # Get objects tags
                for t in tags: # Loop through tags
                    if t.GetTypeName() == "Texture": # If Texture tag founded
                        objname = x.GetName() # Get object's name
                        mat = t.GetMaterial() # Get material
                        matname = mat.GetName() # Get material name
                        copy = mat.GetClone() # Clone material
                        copy.SetName(objname+"_"+matname) # Set cloned material name
                        doc.InsertMaterial(copy) # Insert cloned material to document
                        doc.AddUndo(c4d.UNDOTYPE_NEW, copy)
                        doc.AddUndo(c4d.UNDOTYPE_CHANGE, t)
                        t.SetMaterial(copy) # Set cloned material to object's texture tag
    except: # If something went wrong
        pass # Do nothing
    doc.EndUndo() # Stop recording undos
    c4d.EventAdd() # Refresh Cinema 4D

# Execute main()
if __name__=='__main__':
    main()