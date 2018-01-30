import os
import sys
import logging
import json

from Bio.Blast import NCBIXML
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
from Bio import SeqIO

# ====================================================================================
# FUNTIONS
# ====================================================================================

def determine_path():
    try:
        root = __file__
        if os.path.islink(root):
            root = os.path.realpath(root)
        return os.path.dirname(os.path.abspath(root))
    except:
        print("I'm sorry, but something is wrong.")
        print("There is no __file__ variable. Please contact the author.")
        sys.exit()

def get_data_version():
	data_version = ""
	card_json_path = os.path.join(data_path,"card.json")
	if os.path.isfile(card_json_path) == True:
		with open(card_json_path) as json_file:
			json_data = json.load(json_file)
			for item in json_data.keys():
				if item == "_version":
					data_version = json_data[item]

	if data_version == "":
		logger.error('data file card.json not found in data path: {}. \nPlease download card.json from https://card.mcmaster.ca/download. \nSee `rgi load --help` to upload the card.json to rgi application.\n'.format(data_path))

	return data_version


# ====================================================================================
# FILEPATHS
# ====================================================================================

script_path = determine_path()

path = os.path.join(script_path, "_db/")
data_path = os.path.join(script_path, "_data/")
tmp = os.path.join(script_path, "_tmp/")
logs = os.path.join(script_path, "_logs/")


# ====================================================================================
# LOGGING CONFIG
# ====================================================================================

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

formatter = logging.Formatter('%(levelname)s %(asctime)s : (%(filename)s::%(funcName)s::%(lineno)d) : %(message)s')

file_handler = logging.FileHandler(os.path.join(logs,"app.log"))
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


DATA_VERSION = get_data_version()
APP_NAME="Resistance Gene Identifier"
SOFTWARE_VERSION = '4.0.0'
SOFTWARE_SUMMARY = 'Use the Resistance Gene Identifier to predict resistome(s) from protein or nucleotide \
data based on homology and SNP models. Check https://card.mcmaster.ca/download for software and data updates. \
Receive email notification of monthly CARD updates via the CARD Mailing List \
(https://mailman.mcmaster.ca/mailman/listinfo/card-l)'
