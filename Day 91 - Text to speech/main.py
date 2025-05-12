# Import the required module for text
# to speech conversion
from gtts import gTTS
from pypdf import PdfReader
from pydub import AudioSegment
from tqdm import tqdm
import os
from os import listdir
from os.path import isfile, join


TMP_FOLDER_PATH = "./tmp"


def concatenate_audio_pydub(audio_clip_paths, output_path, verbose=1):
    """
    Concatenates two or more audio files into one audio file using PyDub library
    and save it to `output_path`. A lot of extensions are supported, more on PyDub's doc.
    """

    def get_file_extension(filename):
        """A helper function to get a file's extension"""
        return os.path.splitext(filename)[1].lstrip(".")

    clips = []
    # wrap the audio clip paths with tqdm if verbose
    audio_clip_paths = (
        tqdm(audio_clip_paths, "Reading audio file") if verbose else audio_clip_paths
    )
    for clip_path in audio_clip_paths:
        # get extension of the audio file
        extension = get_file_extension(clip_path)
        # load the audio clip and append it to our list
        clip = AudioSegment.from_file(clip_path, extension)
        clips.append(clip)

    final_clip = clips[0]
    range_loop = (
        tqdm(list(range(1, len(clips))), "Concatenating audio")
        if verbose
        else range(1, len(clips))
    )
    for i in range_loop:
        # looping on all audio files and concatenating them together
        # ofc order is important
        final_clip = final_clip + clips[i]
    # export the final clip
    final_clip_extension = get_file_extension(output_path)
    if verbose:
        print(f"Exporting resulting audio file to {output_path}")
    final_clip.export(output_path, format=final_clip_extension)


def get_extracted_pages_from_pdf(pdf_path):
    """
    Read text from a PDF file and return it as a list of strings.
    Each string represents the text of a page in the PDF.
    """
    reader = PdfReader(pdf_path)
    extracted_pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            extracted_pages.append(text)
    return extracted_pages


def convert_text_to_audio(extracted_pages):
    """
    Convert a list of text strings to audio files using gTTS.
    Each string in the list will be saved as an audio file.
    """
    for index, text in enumerate(extracted_pages):
        mytext = text
        # Language in which you want to convert
        language = "en"
        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed

        # Creating an object of gTTS
        myobj = gTTS(text=mytext, lang=language, slow=False)

        if not os.path.exists(TMP_FOLDER_PATH):
            os.makedirs(TMP_FOLDER_PATH)
        print(f"Converting page {index} to audio")
        myobj.save(f"./tmp/page-{index}.mp3")
        print(f"Page {index} converted to audio")


reader = PdfReader("Eloquent_JavaScript.pdf")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Simple Audio file combiner using PyDub library in Python"
    )
    parser.add_argument("-f", "--file", help="pdf file path")
    parser.add_argument(
        "-o",
        "--output",
        help="The output audio file, extension must be included (such as mp3, etc.)",
    )
    args = parser.parse_args()
    if not args.file or not args.output:
        print("Please provide the audio clips and output file name")
        exit(1)

    try:
        extracted_pages = get_extracted_pages_from_pdf(args.file)
        print(f"Extracted {len(extracted_pages)} pages from the PDF file")
        convert_text_to_audio(extracted_pages)

        audio_files = [
            f for f in listdir(TMP_FOLDER_PATH) if isfile(join(TMP_FOLDER_PATH, f))
        ]
        audio_files = sorted(
            audio_files, key=lambda x: int(x.split("-")[1].split(".")[0])
        )

        print(f"Audio files to be concatenated: {audio_files}")
        concatenate_audio_pydub(
            [join(TMP_FOLDER_PATH, f) for f in audio_files], args.output, verbose=1
        )
        for f in audio_files:
            os.remove(join(TMP_FOLDER_PATH, f))
        # remove the tmp folder
        if os.path.exists(TMP_FOLDER_PATH):
            os.removedirs(TMP_FOLDER_PATH)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)
    # concatenate the audio files

    # concatenate_audio_pydub(args.file, args.output)
