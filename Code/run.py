import os
from tossing_neo4j_parser import buildGraph
import input_formatter
import stop_stem
import toss_data_extractor
import toss_graph
import tossing_neo4j_parser


def main():

	print ("Checking for output directory `OutputFiles`")
	if not os.path.exists('./OutputFiles'):
		print ("Creating output directory `OutputFiles` ...")
		os.makedirs('./OutputFiles')

	print ("Formatting input... STARTED")
	input_formatter.format_input()
	print ("Formatting input... COMPLETED")

	print ("Stemming and stop-word removal... STARTED")
	preprocessor = stop_stem.Preprocessor()
	preprocessor.process_file()
	print ("Stemming and stop-word removal... COMPLETED")

	print ("Extracting Toss Data... STARTED")
	toss_data_extractor.extract()
	print ("Extracting Toss Data... COMPLETED")

	print ("Preparing Tossing Graph... STARTED")
	tossing_graph = toss_graph.TossingGraph()
	tossing_graph.prepare_graph()
	print ("Preparing Tossing Graph... COMPLETED")

	# print("build Neo4j Graph... STARTED")
	# buildGraph()
	# print("build Neo4j Graph... COMPLETED")

if __name__ == '__main__':
	main()