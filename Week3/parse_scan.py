import xml.etree.ElementTree as ET
import json

def convert_nmap_xml_to_json(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        scan_results = []

        for host in root.findall('host'):
            ip_address = host.find('address').attrib['addr']
            status = host.find('status').attrib['state']
            ports_list = []
            
            for port in host.find('ports').findall('port'):
                port_id = port.attrib['portid']
                protocol = port.attrib['protocol']
                state = port.find('state').attrib['state']
                ports_list.append({"port": port_id, "protocol": protocol, "state": state})
                
            scan_results.append({"ip": ip_address, "status": status, "open_ports": ports_list})

        print(json.dumps(scan_results, indent=4))
        
    except Exception as e:
        print(f"Error parsing XML: {e}")

convert_nmap_xml_to_json('scan_results.xml')