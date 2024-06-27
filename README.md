This app transforms your SBOM CycloneDx json file into a pdf version. 
Pass in the json file as argument to the command. 
and transforms it into a PDF with the same name inside the folder pdf_conversions.
The script creates the folder if it not already created.  

Step 1: run
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py <your_cyclonedx.json>
```

This will then create a PDF called your_filename.pdf
