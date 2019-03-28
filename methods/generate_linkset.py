import csv

#
# -- Program -----------------------------------------------------------------------------------------------------------
#
# Generate the G-NAF Mesh Block Match for Addresses to Mesh Block linkset.
#
# The expected CSV file structure for a row.
#
# ['address_mesh_block_2016_pid', 'address_detail_pid', 'mesh_block_pid', 'date_created', 'mb_match_code']
#

#
# -- Settings ----------------------------------------------------------------------------------------------------------
#

#
# File path to the CSV
#
GNAF_CSV = 'addrmb16-linkset-full.csv'

#
# Only generate 10 rows if True
#
limit_rows = False

#
# -- The program --------------------------------------------------------------------------------------------------------
#

# This changes the GNAF_CSV filename extension to .ttl
OUTPUT_FILE = GNAF_CSV.replace(GNAF_CSV.split('.')[-1], '') + 'ttl'

with open(OUTPUT_FILE, 'w+') as f:
    with open(GNAF_CSV, newline='') as csv_file:
        gnaf = csv.reader(csv_file, delimiter=',', )
        for i, row in enumerate(gnaf):
            if i == 0:
                continue
            if limit_rows and i == 11: # stop printing after 10 rows
                break
            instance = f""":{row[0]}
  s: g:{row[1]} ;
  p: w: ;
  o: b:{row[2]} ;
  m: m{row[4]}: ;
  c: "{row[3]}"^^d: .
"""
            f.write(instance)
