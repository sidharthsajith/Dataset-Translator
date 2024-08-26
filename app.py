import pandas as pd
from deep_translator import GoogleTranslator
from datasets import load_dataset
import concurrent.futures
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def translate_text(translator, text):
    try:
        translated_text = translator.translate(text, target='ml')
        return translated_text
    except Exception as e:
        logger.error(f"Error translating text: {e}")
        return None

def main():
    dataset = load_dataset("tatsu-lab/alpaca")
    mlm_lst = []

    # Create a single translator instance
    translator = GoogleTranslator(source='en')

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(translate_text, translator, text) for text in dataset["train"]["text"]]

        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            logger.info(f"{i} of {len(dataset['train']['text'])} completed")
            mlm_lst.append(future.result())

    df = pd.DataFrame(mlm_lst, columns=['Prompt'])
    logger.info("Translation completed")
    df.to_csv('translated_eng2mlm.csv', encoding="utf-8")

if __name__ == "__main__":
    main()
