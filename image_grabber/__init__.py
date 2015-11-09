import requests
import pprint
import re

from flask import Flask, jsonify, request
from bs4 import BeautifulSoup as BS

pp = pprint.PrettyPrinter(indent=4)


def sort_uris(items, by_file_name=False):

	done = False
	num_items_to_sort = len(items) - 1;
	
	while (done == False):
		
		# initialize done value to true to ensure an already sorted list breaks while loop	
		done = True

		for i in range(num_items_to_sort):
	
			# do sort
			if by_file_name:
				im_one = items[i].split('/');
				im_two = items[i + 1].split('/')
							
				if im_one[len(im_one) - 1].lower() > im_two[len(im_two) - 1].lower():
					items[i], items[i + 1] = items[i + 1], items[i]
					done = False

			else: 	
				if items[i].lower() > items[i + 1].lower():
					items[i], items[i + 1] = items[i + 1], items[i]
					done = False

		# decrement items needing sorted after each interation through list
		num_items_to_sort -= 1

	return items


def count_file_types(imgs, file_types):
	ft_count = {}

	# get file type counts
	for img in imgs:

		ft = file_types[img.split('.')[1].lower()]

		if ft in ft_count:
			ft_count[ft] += 1
		else:
			ft_count[ft] = 1


	return ft_count


def get_images(file_types, filt=False):


	# request homepage and parse image list element
	URI = 'http://deeplocal.com'	
	soup = BS(requests.get(URI).text, 'html.parser')
	imgs = soup.find('ul', class_="photos")

	# create list of image URIs using a regular expression
	imgs = [ i[:len(i) - 1] for i in re.findall('[/].*[?]', str(imgs)) ]

	# check if filter exists and filter by file type if necessary
	if filt:
		imgs = [ i for i in filter(lambda i: i.split('.')[1].lower() in file_types, imgs) ]

	
	return imgs



app = Flask(__name__)


@app.route('/deeplocal/home/images', methods=['GET'])
def get_dl_images():
	try:
		FT = {
			'jpg': ['jpeg', 'jpg'],
			'png': ['png'],
			'gif': ['gif']
		}

		URI = 'http://deeplocal.com'	
	
		# get some request query parameters		
		req_file_types, sort_by_filename, filt = request.args.get('ft'), request.args.get('sbf'), False

		# initialize file type map
		ft_map = { 
			'jpeg': 'jpg',
			'jpg': 'jpg',
			'gif': 'gif', 
			'png': 'png'
		}
	
		# check for request specified file type map	
		if req_file_types:
			ft_map = { k: v for v in [f for f in req_file_types.split(':')] for k in FT[v] }			
			filt = True
	
		# spider page and get sorted list of image URIs	
		imgs = sort_uris(
			get_images(ft_map, filt),
			sort_by_filename
		)

		return jsonify(
			{
				'image_uris': [ (URI + i) for i in imgs ],
                'total': len(imgs),
				'file_types': count_file_types(imgs, ft_map)
			}
		)


	except Exception as e:

		return jsonify(
			{
				'error': 'Ooops, an error occured.'

			}
		)


if __name__ == '__main__':

    app.run(debug=True)
