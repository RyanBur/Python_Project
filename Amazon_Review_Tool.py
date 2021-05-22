'''
Doc String

'''
__author__ = 'Ryan Burakowski'
__version__ = 'Beta'

import numpy as np
import pandas as pd
import re

# Windows cmd line to test is:  
# #python3 Documents\\nycdsa-course\\python_project\\Python_Project\\Amazon_Review_Tool.py

#Get input from user. Can be done in main()

#Create stats on input for analysis (input_analysis())

#Create sample size standard deviation measure for sample size = # reviews,
	# and confidence interval. (sample_size_analysis())

#From cum frequency list, determine where the product falls (percentage-wise). 
	# Also determine th 90% confidence interval for percentages (analysis_results())


# Figure out what to output back to the user based upon the analysis.
	#Might just be in main()


def input_analysis(user_list):
	'''
	Input: User list/string
	Output: tuple: (number of reviews, average rating)
	'''
	total_reviews = sum(user_list)
	average_rating = np.sum(np.array(user_list)*\
		np.array([5,4,3,2,1]))/total_reviews
	return total_reviews, average_rating


def sample_size_analysis(num_reviews):
	'''
	input: # reviews
	output: 90% confidence interval as a float
	'''
	sample_df = pd.read_csv(r'rough_data\amazon_dataset\amzn_confidence_interval_dataset.csv')
	print(sample_df.head(), len(sample_df))


def analysis_results(input_metrics, analysis_metrics, various):
	'''
	Inputs: user list anaysis mtrics, sample analysis metrics
	Output: %-tile for bottom of 90% confidence interval, for average 
	rating, and for top of 90% confidence interval.

	'''
	pass



def main():
	# Write out an intro message
	intro = '\nWelcome to the Amazon product review scoring tool!\n\n'+\
	'This was created by Ryan Burakowski for an NYC Data  Science'+\
	'Academy project. The datset used in this project is for academic '+\
	'purposes only. No commercial use of this tool is allowed.\n'
	# Ask for user input
	intro2 = '\nThis tool will provide information about how the reviews for'+\
		' a specific product on Amazon.com compare to other product reviews on the site.'
	print(intro, intro2)

	# Get reviews from user.
	user_list = []
	for star_num in range(5,0,-1):
		star_count = input(f'Enter the number of {star_num}-star reviews:  ')
		try:
			star_count = int(star_count)
		except:
			raise TypeError('All entered values should be integers')
		user_list.append(star_count)

	# Use helper function to get total reviews and average rating.	
	input_tuple = input_analysis(user_list)
	print(input_tuple)
	ci_interval = sample_size_analysis(input_tuple[0])












if __name__ == '__main__':
	main()
