import FreeSimpleGUI as ui
import zip_extractor

ui.theme("DarkBlue2")

label1 = ui.Text("Select files to extract: ")
input1 = ui.Input()
choose_button_1 = ui.FilesBrowse("Select", key='archive')

label2 = ui.Text("Select destination directory: ")
input2 = ui.Input()
choose_button_2 = ui.FilesBrowse("Select", key='folder')

extract_button = ui.Button("Extract")
output_label = ui.Text(key="output", text_color="green")

window = ui.Window("File Extractor",
                   layout=[[label1, input1, choose_button_1],
                           [label2, input2, choose_button_2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["archive"]
    destin_dir = values["folder"]
    zip_extractor.extract_file(filepath, destin_dir)
    window["output"].update(value="Extraction Completed!")

window.close()