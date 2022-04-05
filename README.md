# Repository for the FateSum project

## Qualitative samples directory 
Contains excel files with different texts and summaries using various models.
These were used for part of the qualitative explorations and were seen as a group.

## Tests directory
Contains quantitative data and experimental tests.

### Data
Contains text-summary pairs from various models on different datasets.
The current nomenclature and way data is organized should be changed.
The filename is of the form {dataset}-{model}-{number of items}-s
The few ending in -all were obtained directly through a github repository and weren't randomly sampled like the other ones.
The data itself is a list of dictionary items that has been pickled through the Pickle module.
The items are of the form {"text": ..., "summary_text": ...} as obtained through the code in f_sampling.py
This is subject to change and could be updated with custom objects as present in f_sampling.py as well.

### Samples
Sample of experiment results shown in .csv format.
The filename is of the form {test type}-{dataset}-{model}-{filter size}
Only drop rate experiments were sampled so far. The filter of "f20" represents that only words appearing 20 times or more in the sample that is tested on will appear in the resulting csv.


### Code
The code itself is mainly present in the form of loosely organized Jupyter notebooks.
The notebooks have been repeatedly used with various models and dataset, but the underlying implementation is unchanged.
process.ipynb includes the code used to import and create the data used for sampling and to be used in tests further on. It uses code from the f_sampling module, which includes helper functions to transform imported texts and summaries into the format explained above in the data section, as well as saving them in different formats.
examples.ipynb was used to generate samples of text/summary pairs to qualitatively analyze.
drop_rate.ipynb includes the code used to conduct the drop rate experiments. The results are good, but the code might be badly optimized. I was not sure what would be a better alternative than many different dictionaries to keep track of large corpora statistics. It still runs relatively fast on datasets with thousands of items.


