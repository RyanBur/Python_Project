'''
Doc String

'''
__author__ = 'Ryan Burakowski'
__version__ = 'Beta'

import numpy as np
import pandas as pd

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

#Complete
def input_analysis(user_list):
	'''
	Input: User list/string
	Output: tuple: (number of reviews, average rating)
	'''
	total_reviews = sum(user_list)
	average_rating = np.sum(np.array(user_list)*\
		np.array([5,4,3,2,1]))/total_reviews
	return total_reviews, average_rating


#Complete
def sample_size_analysis(num_reviews):
	'''
	input: # reviews
	output: 90% confidence interval as a float
	'''
	sample_df = pd.read_csv(r'rough_data\amazon_dataset\amzn_confidence_interval_dataset.csv')

	output_list = []
	for ind in range(5000):
		review_subset = np.random.choice(sample_df['rating'], num_reviews, replace=False)
		avg = review_subset.mean()
		output_list.append(avg)

	series_out = pd.Series(output_list)
	# Standard dev of the samples
	std = np.std(series_out)
	# z-score for 90% confidence interval
	z_score = 1.645
	#90% confidence interval
	c_i_range = z_score * std
	return round(c_i_range,3)
	

#Complete
def analysis_results(c_i_range, average_rating):
	'''
	Inputs: user list anaysis mtrics, sample analysis metrics
	Output: %-tile for bottom of 90% confidence interval, for average 
	rating, and for top of 90% confidence interval.
	'''
	cum_freq_df = pd.read_csv(r'rough_data\amazon_dataset\amzn300_cum_freq_table.csv')
	# Confidence interval endpoints, and average, rounded to align with the
		# values in the frequency table and bounded by the table limits. 
	low_c_i = max(round((average_rating - c_i_range)/2,2)*2,1.02)
	high_c_i = min(round((average_rating + c_i_range)/2,2)*2,5)
	average_rating = round(average_rating/2,2)*2

	# Retrieve the corresponding cumulative frequency
	low_ci_rating = cum_freq_df[cum_freq_df['star_rating'] \
		== low_c_i].iloc[0,1]
	average_rating_num = cum_freq_df[cum_freq_df['star_rating'] \
		== average_rating].iloc[0,1]
	high_ci_rating = cum_freq_df[cum_freq_df['star_rating'] \
		== high_c_i].iloc[0,1]
	# Turn them into percents
	low_ci_percent = round(low_ci_rating*100)
	average_rating_percent = round(average_rating_num*100)
	high_ci_percent = round(high_ci_rating*100)
	return low_ci_percent, average_rating_percent, high_ci_percent



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

	# Use helper functions to conduct all the analysis.	
	input_tuple = input_analysis(user_list)
	c_i_range = sample_size_analysis(input_tuple[0])
	low_end_ci, actual_result, high_end_ci = \
		analysis_results(c_i_range, input_tuple[1])

	#Logic for printing result. 
	print('='*20, '\n      Results')
	print('='*20)
	if (high_end_ci - low_end_ci) > 25 and input_tuple[0] < 300:
		msg = f'Product average rating is better than {actual_result}% of' +\
			' products on Amazon. \nHowever, because of the relatively small' +\
			' number of reviews, it is only 90% certain that the product is' +\
			f' better than between {low_end_ci}% to {high_end_ci}% of Amazon' +\
			' products. To tighten this range, it is recommended that a product' +\
			' have at least 300 reviews before using this tool.'
		print(msg)
	else:
		msg = f'Product average rating is better than {actual_result}% of products ' +\
			'on Amazon. \nStatistically, there is a 90% certainty that the product is' +\
			f' better than between {low_end_ci}% to {high_end_ci}% of Amazon ' +\
			'products. Running this tool when the product has more reviews will' +\
			' help tighten this range.'
		print(msg)
		
		
	print('\naverage rating:', \
		round(input_tuple[1],2), '\nconfidence interval:', \
			c_i_range, '\nnumber of reviews:', input_tuple[0])












if __name__ == '__main__':
	main()
