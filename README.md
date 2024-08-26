# Translation of English Text to Malayalam using Deep Translator and Datasets
This documentation provides an overview of the code used to translate English text to Malayalam using the Deep Translator library and the Datasets library.

# Overview
The code is designed to translate a dataset of English text (alpaca for example here) to any language (currently Hindi) using the Google Translator API. The translation process is performed in parallel using multiple threads, which improves the speed and efficiency of the translation process.

### List of Languages to Translate to
1) Run this snippet of code to get the list of available languages
```python
from deep_translator import GoogleTranslator
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
```
2) Now replace `hi` in the code to the desired language from the above output.

# Components
## Libraries
* pandas (pd): A library for data manipulation and analysis.
* deep_translator: A library for machine translation.
* datasets: A library for loading and manipulating datasets.
* concurrent.futures: A library for parallel processing.
* logging: A library for logging and debugging.
## Functions
* `translate_text`(translator, text): A function that translates a given text using the Google Translator API.
* `main()`: The main function that loads the dataset, creates a translator instance, and performs the translation process in parallel.
## Variables
* `dataset`: The dataset loaded from the tatsu-lab/alpaca dataset.
* `mlm_lst`: A list to store the translated text.
* `translator`: A single instance of the Google Translator API.
* `executor`: A thread pool executor used for parallel processing.
* `futures`: A list of futures representing the translation tasks.
* `i`: A counter used to track the progress of the translation process.
* `future`: A future representing the result of a translation task.
* `logger`: A logger used for logging and debugging.
# Code Flow
- The code starts by loading the dataset using the load_dataset function from the Datasets library.
- It creates a single instance of the Google Translator API using the GoogleTranslator class from the Deep Translator library.
```python
def translate_text(translator, text):
    try:
        translated_text = translator.translate(text, target='hi')
        return translated_text
    except Exception as e:
        logger.error(f"Error translating text: {e}")
        return None
```
- It creates a thread pool executor using the ThreadPoolExecutor class from the concurrent.futures library, with a maximum of 10 workers.
```python
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(translate_text, translator, text) for text in dataset["train"]["text"]]
```
- It submits the translation tasks to the executor using the submit method, which returns a list of futures.
- It iterates over the futures using the as_completed method, which returns an iterator over the futures as they complete.
- For each future, it logs the progress of the translation process and appends the result to the mlm_lst list.
- Once all the futures have completed, it creates a Pandas DataFrame from the mlm_lst list and saves it to a CSV file named translated_eng2mlm.csv.
## Logging
The code uses the logging library to log the progress of the translation process and any errors that may occur during the translation process. The logging level is set to INFO, which means that only important messages will be logged.

## Conclusion
This code provides a simple and efficient way to translate English text to Malayalam using the Deep Translator library and the Datasets library. The parallel processing capabilities of the concurrent.futures library improve the speed and efficiency of the translation process.
