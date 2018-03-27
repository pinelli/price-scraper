import xml_r_w

SHOPS_PATH = "shops.xml"
sitesL = xml_r_w.read_sites(SHOPS_PATH)
print("Shops ", sitesL)
