from os import path
# from shutil import copyfile
from xml.etree import ElementTree

CURRENT_DIR = path.dirname(path.realpath(__file__))

WORKSPACE_FILE = "../../.idea/workspace.xml"
WORKSPACE_TEMPLATE_FILE = "idea_default_run_manager.xml"

if __name__ == '__main__':
    work_space_file_path = path.join(CURRENT_DIR, WORKSPACE_FILE)
    root = ElementTree.parse(work_space_file_path).getroot()
    element = ElementTree.parse(path.join(CURRENT_DIR, WORKSPACE_TEMPLATE_FILE)).getroot()
    root.insert(-1, element)
    with open(".idea/workspace.xml", "w") as file:
        file.write(ElementTree.tostring(root).decode("utf-8"))
    print("Your workspace updated.")
