letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''
            
# yaha hame nake ke place pe name or date ke place pe date likhni h
print(letter.replace("<|Name|>","Ishita").replace("<|Date|>","9 june 2025"))  
#yaha hame uper chaining ke h replace ke name ke saath hame date bhe change karni thi to hamne jab name change kara to waha humne saath me next chain bana ke ek or replace de diya date ke liye
