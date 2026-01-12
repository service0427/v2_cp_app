from adb_naver_automation.core.engine import AutomationEngine
import xml.etree.ElementTree as ET
import sys
import argparse

# Configuration
DEVICE_ID = "RF9XC00EXGM"

class UIInspector(AutomationEngine):
    def inspect(self):
        print("[Inspector] Capturing Screenshot & UI Hierarchy...")
        
        # 1. Capture Screenshot
        local_png = "inspector_capture.png"
        self.run_adb(["shell", "screencap", "-p", "/sdcard/inspector_capture.png"])
        self.run_adb(["pull", "/sdcard/inspector_capture.png", local_png])
        
        # 2. Dump UI
        self.dump_ui()
        content = self.get_ui_content()
        
        if not content:
            print("[Error] Failed to get UI content.")
            return

        self.parse_and_report(content)
        print(f"\n[Screenshot Saved]: {local_png}")

    def parse_and_report(self, xml_content):
        print("\n" + "="*50)
        print("       CURRENT SCREEN ANALYSIS Report")
        print("="*50)
        
        try:
            root = ET.fromstring(xml_content)
        except ET.ParseError:
            print("[Error] XML Parse Error.")
            return

        packages = set()
        texts = []
        # Mapping: Resource ID -> {Text, Bounds}
        elements_info = {}
        
        # Recursively find all nodes
        for node in root.iter():
            pkg = node.attrib.get('package')
            text = node.attrib.get('text')
            res_id = node.attrib.get('resource-id')
            bounds = node.attrib.get('bounds')
            
            if pkg: packages.add(pkg)
            if text: texts.append(text)
            if res_id: 
                elements_info[res_id] = {'text': text, 'bounds': bounds}

        print(f"\n[1] Active Packages: {list(packages)}")
        
        print(f"\n[2] Visible Texts (Count: {len(texts)}):")
        print("-" * 30)
        for t in texts:
            print(f"  • {t}")
            
        print(f"\n[3] Interactable Resource IDs (Count: {len(elements_info)}):")
        print("-" * 30)
        for r in sorted(elements_info.keys()):
            info = elements_info[r]
            note = f" ('{info['text']}')" if info['text'] else ""
            bounds_str = f" {info['bounds']}" if info['bounds'] else ""
            print(f"  • {r}{bounds_str}{note}")
            
        print("\n" + "="*50)

def main():
    parser = argparse.ArgumentParser(description="Naver App UI Inspector")
    parser.add_argument("--device-id", default=DEVICE_ID, help="Target Device Serial")
    args = parser.parse_args()

    inspector = UIInspector(args.device_id)
    inspector.inspect()

if __name__ == "__main__":
    main()
