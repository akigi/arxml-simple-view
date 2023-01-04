import xml.etree.ElementTree as ET
import re
import sys
from pathlib import Path

class ARXML_SIMPLE_VIEW:
    def __init__(self, arxml_path) -> None:
        self.arxml_path = arxml_path
        self.tree = None
        self.root = None
        self.ns:str = ""


    def __get_namespace(self, element):
        m = re.match(r'\{.*\}', element.tag)
        return m.group(0) if m else ''            

    def simplify(self, output_path=None, arxml_path=None, **kwargs):
        if arxml_path is None:
            arxml_path = self.arxml_path
        
        tree = ET.parse(arxml_path)
        self.tree = tree

        root = tree.getroot()
        self.root = root

        ns = self.__get_namespace(root)
        self.ns = ns

        if output_path is None:
            f = None
        else:
            f = open(output_path, "w", encoding="utf_8_sig")

        self.__rep(root, -1, f, **kwargs)

        if f:
            f.close()
            
    def __rep(self, parent, indent_parent=-1, fp=None, pattern=6):
        indent = indent_parent + 1
        
        short_name = ""
        ns = self.ns
        if sne:= parent.findall(f"{ns}SHORT-NAME"):
            short_name = sne[0].text

        tabstr = "\t"

        if pattern == 1:
            write_text = f"{tabstr*indent}{parent.tag.replace(ns, '')} {short_name}"
        elif pattern == 2:    
            write_text = f"{tabstr*indent}[{parent.tag.replace(ns, '')}] {short_name}"
        elif pattern == 3:
            if not short_name:
                write_text = f"{tabstr*indent}{parent.tag.replace(ns, '')}"
            else:
                write_text = f"{tabstr*indent}{parent.tag.replace(ns, '')} ({short_name})"
        elif pattern == 4:
            if not short_name:
                write_text = f"{tabstr*indent}{parent.tag.replace(ns, '')}"
            else:
                write_text = f"{tabstr*indent}{short_name}"
        elif pattern == 5:
            if not short_name:
                write_text = f"{tabstr*indent}{parent.tag.replace(ns, '')}"
            else:
                write_text = f"{tabstr*indent}{parent.tag.replace(ns, '')} [{short_name}]"
        elif pattern == 6:
            if not short_name:
                write_text = f"{tabstr*indent}<{parent.tag.replace(ns, '')}>"
            else:
                write_text = f"{tabstr*indent}<{parent.tag.replace(ns, '')}> [{short_name}]"

        if fp:
            fp.write(write_text + "\n")
        else:
            print(write_text)

        for child in parent:
            self.__rep(child, indent, fp, pattern)



if __name__ == "__main__":
    paths = list(map(Path, sys.argv[1:]))
    for path in paths:
        output_path = Path(str(path)+".simple.txt")
        sv = ARXML_SIMPLE_VIEW(path)
        sv.simplify(output_path)

    
    
    