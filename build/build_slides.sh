#!/bin/sh



all_notebooks=$(find ../src_EN -iname "*.ipynb" -iname "B3*" -not -iname "*checkpoint.ipynb")


for notebook_path in ${all_notebooks}
do
	file_dir=$(dirname "${notebook_path}")
	file_name=$(basename "${notebook_path}")
	extension="${file_name##*.}"   # .ipynb
	file_name="${file_name%.*}"
	
	cd ${file_dir}
	
	echo ${file_name}
	jupyter nbconvert ${file_name}.ipynb  --execute --allow-errors --to slides --template reveal_custom --SlidesExporter.reveal_number='c' --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags=opt --ExecutePreprocessor.skip_cells_with_tag=no_run
	chromium --headless --print-to-pdf=${file_name}.pdf "file://$(realpath ${file_name}.slides.html)?print-pdf"
	rm ${file_name}.slides.html
	cd -
done


# --execute --allow-errors
