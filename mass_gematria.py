import sys

from gematria_values import *

# Constants
ALL_GEMATRIA_TYPES = [l_ordinal, l_reduction, l_reverse, l_reverse_reduction]
ALL_GEMATRIA_NAMES = ["Ordinal", "Reduction", "Reverse", "Reverse-Reduction"]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
PUNCTUATION = [',', '\'', '.', '\"', ':', ';', '(', ')', '[', ']', '{', '}', '/', '!',
	'?', '<', '>', '#', '$', '%', '^', '&', '*', '~', '`']


checked_words = [] #


def calculate_gematria(input_text, number_to_match) -> ([str], str):
	# Returns the type of Gematria match made and the (cleaned up) input word
	# Returns [[], input_text] if there are no matches
	matches = []

	# Swapping out alt chars (usually with diacritics) with their standard Latin equivalents
	for c, char in enumerate(input_text):
		if char in l_replacement.keys():
			input_text = input_text[:c] + l_replacement[char] + input_text[c+1:]

	if input_text not in checked_words:
		checked_words.append(input_text)

		# Doing math
		for g, gematria_type in enumerate(ALL_GEMATRIA_TYPES):
			total_value = 0
			for char in input_text:
				if char in gematria_type.keys():
					total_value += gematria_type[char]
				elif char in NUMBERS:
					total_value += int(char)
			if total_value == number_to_match:
				matches.append(ALL_GEMATRIA_NAMES[g])

	return (matches, input_text)


if __name__ == "__main__":
	# sys.argv[1] is the number to match, sys.argv[2] is the filename
	# ex. "python mass_gematria.py 47 words.txt"
	with open(sys.argv[2]) as file:
		# Breaks up the file by line breaks and spaces
		file_broken = file.read().replace(' ', '\n')
		file_lines = file_broken.split('\n')
		print(f"\nMASS GEMATRIA CHECK")
		print(f"Finding words with a value of {int(sys.argv[1])} in file {sys.argv[2]}\n")
		print(f"Checking gematria systems:")
		for gematria_name in ALL_GEMATRIA_NAMES:
			print(f"- {gematria_name}")
		print("\n"+'-'*48+'\n')

		match_counter = 0
		for line in file_lines:
			line = line.strip().lower()

			# Remove punctuation
			for char in line:
				if char in PUNCTUATION:
					line = line.replace(char, '')
			matching_gematria = calculate_gematria(line, int(sys.argv[1]))

			# Print matching strings
			if len(matching_gematria) > 0:
				for gematria_type in matching_gematria[0]:
					print(f"-	{matching_gematria[1]} -- {gematria_type} ({str(sys.argv[1])})")
					match_counter += 1

		print("\n"+'-'*48+'\n')
		print(f"Finished, {str(match_counter)} total matches.\n")