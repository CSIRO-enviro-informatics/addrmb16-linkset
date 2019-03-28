SELECT
	gnaf.address_mesh_block_2016.address_mesh_block_2016_pid,
	gnaf.address_mesh_block_2016.address_detail_pid,
	SUBSTRING(gnaf.address_mesh_block_2016.mb_2016_pid, 5) AS mesh_block_pid,
	gnaf.address_mesh_block_2016.date_created,
	gnaf.address_mesh_block_2016.mb_match_code
FROM gnaf.address_mesh_block_2016