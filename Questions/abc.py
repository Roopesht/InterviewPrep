def SharewithWhatsapp(text: str):
    #format text as per whatsapp formatting
    
    # replace the lines starting with '#' with * on both the sides
    for line in text.split("\n"):
        if line.startswith("# "):
            text = text.replace(line, "*" + line[2:] + "*")

    # replace the lines starting with '##' with _ on both the sides
    for line in text.split("\n"):
        if line.startswith("## "):
            text = text.replace(line, "_" + line[3:] + "_")
    
    

